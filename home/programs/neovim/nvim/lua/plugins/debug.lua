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

vim.api.nvim_create_user_command("PythonAttach", function(opts)
    python_attach({ remote_root = opts.fargs[1] or vim.fn.getcwd() })
end, {
    nargs = "*",
    complete = "file_in_path",
})

return {
    "rcarriga/nvim-dap-ui",
    cond = is_not_mini,
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
    },
    config = function()
        local dap, dapui = require("dap"), require("dapui")
        dapui.setup()
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
            "<Leader>db",
            function()
                require("dap").toggle_breakpoint()
            end,
            desc = "Dap: ToggleBreakpoint",
        },
        {
            "<Leader>dB",
            function()
                require("dap").set_breakpoint()
            end,
            desc = "Dap: SetBreakpoint",
        },
        {
            "<Leader>dr",
            function()
                require("dap").repl.open()
            end,
            desc = "Dap: Repl",
        },
        {
            "<Leader>dl",
            function()
                require("dap").run_last()
            end,
            desc = "Dap: run last",
        },
        {
            "<Leader>dh",
            function()
                require("dap.ui.widgets").hover()
            end,
            desc = "Dap: Hover",
            mode = { "n", "v" },
        },
        {
            "<Leader>dp",
            function()
                require("dap.ui.widgets").preview()
            end,
            desc = "Dap: Preview",
            mode = { "n", "v" },
        },
        {
            "<Leader>df",
            function()
                local widgets = require("dap.ui.widgets")
                widgets.centered_float(widgets.frames)
            end,
            desc = "Dap: Frames",
        },
        {
            "<Leader>ds",
            function()
                local widgets = require("dap.ui.widgets")
                widgets.centered_float(widgets.scopes)
            end,
            desc = "Dap: Scopes",
        },
        {
            "<Leader>de",
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
    cmd = { "PythonAttach" },
}
