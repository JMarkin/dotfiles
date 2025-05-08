return {
  "ThePrimeagen/refactoring.nvim",
  keys = {
    {
      "<leader>cr",
      mode = { "n", "v" },
      function()
        require("refactoring").select_refactor()
      end,
      desc = "Select for Refactor",
    },
  },
  config = function()
    require("refactoring").setup({
      show_success_message = true,
    })
  end,
}
