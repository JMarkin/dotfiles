vim.g.neovide_transparency = 0.85
vim.g.neovide_input_macos_option_key_is_meta = "both"
vim.g.neovide_window_blurred = true
vim.g.neovide_remember_window_size = false
vim.g.neovide_input_use_logo = 1
vim.g.neovide_unlink_border_highlights = true


-- stylua: ignore start
vim.cmd([[
    cmap <D-v> <C-r>+
    map <D-v> "+p<CR>
    map! <D-v> <C-R>+
    tmap <D-v> <C-v>
    vmap <D-c> "+y<CR>

    map ˙ <a-h>
    map ∆ <a-j>
    map ˚ <a-k>
    map ¬ <a-l>
    map ƒ <a-f>
    map © <a-g>
    tmap © <a-g>
    map † <a-t>
    tmap † <a-t>
    map ∫ <a-b>
    tmap ∫ <a-b>
    map ˆ <a-i>
    tmap ˆ <a-i>
]])
-- stylua: ignore end

vim.g.neovide_scale_factor = 1.0
local change_scale_factor = function(delta)
    vim.g.neovide_scale_factor = vim.g.neovide_scale_factor + delta
    vim.cmd(":redraw!")
end
vim.keymap.set("n", "<C-=>", function()
    change_scale_factor(0.25)
end)
vim.keymap.set("n", "<C-->", function()
    change_scale_factor(-0.25)
end)

-- local colors = {
--     "#10100E",
--     "#0087BD",
--     "#20B2AA",
--     "#009F6B",
--     "#9A4EAE",
--     "#C40233",
--     "#C6C6C4",
--     "#FFD700",
--     "#696969",
--     "#007FFF",
--     "#00CCCC",
--     "#03C03C",
--     "#FF1493",
--     "#FF2400",
--     "#FFFAFA",
--     "#FDFF00",
-- }
--
-- for index, value in ipairs(colors) do
--     vim.g[string.format("terminal_color_%s", 15 - index)] = value
-- end
