local is_not_mini = require("funcs").is_not_mini

local python_attach = function(options)
    local dap = require("dap")
    options = {
        host = options.host or "0.0.0.0",
        port = options.port or 5678,
        remote_root = options.remote_root or "/app",
    }
    local host = options.host -- This should be configured for remote debugging if your SSH tunnel is setup.
    -- You can even make nvim responsible for starting the debugpy server/adapter:
    --  vim.fn.system({"${some_script_that_starts_debugpy_in_your_container}", ${script_args}})
    local pythonAttachAdapter = {
        type = "server",
        host = host,
        port = options.port,
    }
    local pythonAttachConfig = {
        type = "python",
        request = "attach",
        connect = {
            port = options.port,
            host = host,
        },
        mode = "remote",
        name = "Remote Attached Debugger",
        cwd = vim.fn.getcwd(),
        pathMappings = {
            {
                localRoot = vim.fn.getcwd(), -- Wherever your Python code lives locally.
                remoteRoot = options.remote_root, -- Wherever your Python code lives in the container.
            },
        },
    }
    local session = dap.attach(pythonAttachAdapter, pythonAttachConfig)
    if session == nil then
        io.write("Error launching adapter")
    end
    require("dapui").open()
end

vim.api.nvim_create_user_command("PythonRemoteAttach", function(opts)
    python_attach({ remote_root = opts.fargs[1] or vim.fn.getcwd() })
end, {
    nargs = "*",
    complete = "file_in_path",
})

return {
    "rcarriga/nvim-dap-ui",
    cond = is_not_mini,
    lazy = true,
    dependencies = {
        {
            "mfussenegger/nvim-dap",
        },
        {
            "theHamsta/nvim-dap-virtual-text",
            opts = {},
            dependencies = "nvim-treesitter",
        },
        "ofirgall/goto-breakpoints.nvim",
        {
            "LiadOz/nvim-dap-repl-highlights",
            dependencies = "nvim-treesitter",
        },
        "mfussenegger/nvim-dap-python",
        "leoluz/nvim-dap-go",
    },
    config = function()
        local dap, dapui = require("dap"), require("dapui")
        require("dap-python").setup(require("utils.python_venv").getPythonEnv())
        require("dap-go").setup()

        dapui.setup({
            mappings = {
                -- Use a table to apply multiple mappings
                expand = { "<CR>", "<2-LeftMouse>", "za" },
            },
            controls = {
                enabled = vim.fn.exists("+winbar") == 1,
                element = "repl",
                icons = {
                    pause = "",
                    play = "(F5)",
                    step_into = "(F11)",
                    step_over = "(F10)",
                    step_out = "(F12)",
                    step_back = "(F9)",
                    run_last = "(<leader>dl)",
                    terminate = "",
                    disconnect = "",
                },
            },
            layouts = {
                {
                    -- You can change the order of elements in the sidebar
                    elements = {
                        -- Provide IDs as strings or tables with "id" and "size" keys
                        { id = "breakpoints", size = 0.1 },
                        { id = "watches", size = 0.1 },
                        {
                            id = "scopes",
                            size = 0.45, -- Can be float or integer > 1
                        },
                        { id = "stacks", size = 0.25 },
                    },
                    size = 40,
                    position = "left", -- Can be "left" or "right"
                },
                {
                    elements = {
                        "repl",
                        "console",
                    },
                    size = 10,
                    position = "bottom", -- Can be "bottom" or "top"
                },
            },
        })
        dap.listeners.after.event_initialized["dapui_config"] = function()
            dapui.open()
        end
        dap.listeners.before.event_terminated["dapui_config"] = function()
            dapui.close()
        end
        dap.listeners.before.event_exited["dapui_config"] = function()
            dapui.close()
        end

        require("nvim-dap-repl-highlights").setup()
    end,
    keys = {
        {
            "<leader>dc",
            function()
                require("dapui").close()
            end,
            desc = "Dap: UIClose",
        },
        {
            "<leader>do",
            function()
                require("dapui").open()
            end,
            desc = "Dap: UIOpen",
        },
        {
            "<leader>dd",
            function()
                require("dapui").toggle()
            end,
            desc = "Dap: UIToggle",
        },
        {
            "<F5>",
            function()
                require("dap").continue()
            end,
            desc = "Dap: continue",
        },
        {
            "<F10>",
            function()
                require("dap").step_over()
            end,
            desc = "Dap: step over",
        },
        {
            "<F11>",
            function()
                require("dap").step_into()
            end,
            desc = "Dap: step into",
        },
        {
            "<F12>",
            function()
                require("dap").step_out()
            end,
            desc = "Dap: step out",
        },
        {
            "<F9>",
            function()
                require("dap").step_back()
            end,
            desc = "Dap: step back",
        },
        {
            "<leader>db",
            function()
                require("dap").toggle_breakpoint()
            end,
            desc = "Dap: ToggleBreakpoint",
        },
        {
            "<leader>dB",
            function()
                require("dap").set_breakpoint()
            end,
            desc = "Dap: SetBreakpoint",
        },
        {
            "<leader>dr",
            function()
                require("dap").repl.open()
            end,
            desc = "Dap: Repl",
        },
        {
            "<leader>dl",
            function()
                require("dap").run_last()
            end,
            desc = "Dap: run last",
        },
        {
            "<leader>dh",
            function()
                require("dap.ui.widgets").hover()
            end,
            desc = "Dap: Hover",
            mode = { "n", "v" },
        },
        {
            "<leader>dp",
            function()
                require("dap.ui.widgets").preview()
            end,
            desc = "Dap: Preview",
            mode = { "n", "v" },
        },
        {
            "<leader>df",
            function()
                local widgets = require("dap.ui.widgets")
                widgets.centered_float(widgets.frames)
            end,
            desc = "Dap: Frames",
        },
        {
            "<leader>ds",
            function()
                local widgets = require("dap.ui.widgets")
                widgets.centered_float(widgets.scopes)
            end,
            desc = "Dap: Scopes",
        },
        {
            "<leader>de",
            function(...)
                require("dapui").float_element(...)
            end,
            desc = "Dap: UIFloatElement",
            mode = "v",
        },
        {
            "<leader>dE",
            function(...)
                require("dapui").eval(...)
            end,
            desc = "Dap: Eval",
            mode = "v",
        },
        {
            "]D",
            function()
                require("goto-breakpoints").next()
            end,
            desc = "Next breakkpoint",
        },
        {
            "[D",
            function()
                require("goto-breakpoints").prev()
            end,
            desc = "Prev breakkpoint",
        },
        {
            "]S",
            function()
                require("goto-breakpoints").stopped()
            end,
        },
    },
    cmd = { "PythonRemoteAttach" },
}
