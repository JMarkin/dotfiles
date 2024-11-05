local setup_kubectl = function()
    local opts = {}
    if vim.g.kubeconfig ~= nil then
        opts.kubectl_cmd = {
            cmd = "kubectl",
            env = { KUBECONFIG = vim.g.kubeconfig },
            args = {},
        }
    end
    require("kubectl").setup(opts)
end

return {
    {
        "ramilito/kubectl.nvim",
        cmd = { "Kubectl", "Kubectx", "Kubens" },
        config = setup_kubectl,
        keys = {
            {
                "<space>k",
                function()
                    local out = vim.system(
                        { "fd", "-a", "--glob", "*yaml", vim.env.HOME .. "/.kube/configs" },
                        { text = true }
                    )
                        :wait()
                    local selects = {}
                    for segment in string.gmatch(out.stdout, "[^\n]+") do
                        table.insert(selects, segment)
                    end

                    vim.ui.select(selects, {
                        prompt = "Select kubeconfig:",
                        format_item = function(item)
                            return item
                        end,
                    }, function(choice)
                        vim.g.kubeconfig = choice
                        setup_kubectl()
                        require("kubectl").toggle()
                    end)
                end,
                noremap = true,
                silent = true,
            },
        },
    },
}
