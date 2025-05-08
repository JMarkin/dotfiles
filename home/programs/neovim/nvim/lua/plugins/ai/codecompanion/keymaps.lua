return {
  options = {
    modes = {
      n = "?",
    },
    callback = "keymaps.options",
    description = "Options",
    hide = true,
  },
  completion = {
    modes = {
      i = "<C-_>",
    },
    index = 1,
    callback = "keymaps.completion",
    description = "Completion Menu",
  },
  send = {
    modes = {
      n = { "<CR>", "<C-s>" },
      i = "<C-s>",
    },
    index = 1,
    callback = "keymaps.send",
    description = "Send",
  },
  regenerate = {
    modes = {
      n = "gr",
    },
    index = 2,
    callback = "keymaps.regenerate",
    description = "Regenerate the last response",
  },
  close = {
    modes = {
      n = "<C-c>",
      i = "<C-c>",
    },
    index = 3,
    callback = "keymaps.stop",
    description = "Stop Chat",
  },
  stop = {
    modes = {
      n = "q",
    },
    index = 4,
    callback = "keymaps.stop",
    description = "Stop Request",
  },
  clear = {
    modes = {
      n = "gx",
    },
    index = 5,
    callback = "keymaps.clear",
    description = "Clear Chat",
  },
  codeblock = {
    modes = {
      n = "gc",
    },
    index = 6,
    callback = "keymaps.codeblock",
    description = "Insert Codeblock",
  },
  yank_code = {
    modes = {
      n = "gy",
    },
    index = 7,
    callback = "keymaps.yank_code",
    description = "Yank Code",
  },
  next_chat = {
    modes = {
      n = "}",
    },
    index = 8,
    callback = "keymaps.next_chat",
    description = "Next Chat",
  },
  previous_chat = {
    modes = {
      n = "{",
    },
    index = 9,
    callback = "keymaps.previous_chat",
    description = "Previous Chat",
  },
  next_header = {
    modes = {
      n = "]]",
    },
    index = 10,
    callback = "keymaps.next_header",
    description = "Next Header",
  },
  previous_header = {
    modes = {
      n = "[[",
    },
    index = 11,
    callback = "keymaps.previous_header",
    description = "Previous Header",
  },
  change_adapter = {
    modes = {
      n = "ga",
    },
    index = 12,
    callback = "keymaps.change_adapter",
    description = "Change adapter",
  },
  fold_code = {
    modes = {
      n = "za",
    },
    index = 13,
    callback = "keymaps.fold_code",
    description = "Fold code",
  },
  debug = {
    modes = {
      n = "gd",
    },
    index = 14,
    callback = "keymaps.debug",
    description = "View debug info",
  },
  system_prompt = {
    modes = {
      n = "gs",
    },
    index = 15,
    callback = "keymaps.toggle_system_prompt",
    description = "Toggle the system prompt",
  },
}
