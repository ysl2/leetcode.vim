# leetcode.vim

[![asciicast][thumbnail]][asciicast]

Solve LeetCode problems in Vim!

This Vim plugin is a fork of [ianding1/leetcode.vim][leetcode.vim] which is inspired by [skygragon/leetcode-cli][leetcode-cli].

**Attention:** Recently LeetCode used Google reCAPTCHA to enhance security,
prohibiting automatic login through LeetCode API.

The new login procedure needs you to **login in your browser first** so that

**leetcode.vim** can read the LeetCode session cookie from the browser's cookie
storage.

Supported browsers are: **Chrome**, **Firefox**. Safari is not supported
yet.

## Installation

1. Vim with `+python3` feature is **required**. Install the **pynvim** package
for Neovim:
```sh
pip3 install pynvim --user
```
2. Install the plugin:

plug
```vim
Plug 'ysl2/leetcode.vim', { 'do': 'pip3 install -r requirements.txt' }

```
packer
```lua
use({ "ysl2/leetcode.vim", run = "pip3 install -r requirements.txt" })

```

3. Set `g:leetcode_browser` to `'chrome'` or `'firefox'`.

## Quick Start

- `:LeetCodeList`: browse the problems.
- `:LeetCodeTest`: run the code with the default test case.
- `:LeetCodeSubmit`: submit the code.

## Local Code
When test and submit, match `local end` to last. You can add your local code before `//local end`.

## Key mappings

**leetcode.vim** doesn't bind any key mappings by default. Put the following
lines to your **.vimrc** to set up the key mappings.

```vim
nnoremap <leader>ll :LeetCodeList<cr>
nnoremap <leader>lt :LeetCodeTest<cr>
nnoremap <leader>ls :LeetCodeSubmit<cr>
```

## Customization

### `g:leetcode_china`

When non-zero, use LeetCode China accounts instead.

Default value is `0`.

### `g:leetcode_solution_filetype`

The preferred programming language.

Values: `'c'`, `'cpp'`, `'csharp'`, `'java'`, `'kotlin'`, `'scala'`, `'python'`, `'python3'`, `'ruby'`, `'javascript'`, `'typescript'`, `'php'`,
`'swift'`, `'rust'`, `'golang'`, `'erlang'`, `'racket'`, `'erlang'`.

Default value is `'golang'`.

### `g:leetcode_browser`

Set to the browser that stores the LeetCode session cookie.

Values: `'disabled'`, `'chrome'`, `'firefox'`

Default value is `'disabled'`.

### `g:leetcode_hide_paid_only`

Hide the paid only problems on the list.

Default value is `0`.

### `g:leetcode_hide_topics`

Hide the topics section.

Default value is `0`

### `g:leetcode_hide_companies`

Hide the companies section.

Default value is `0`

### `g:leetcode_problemset`

Set the problemset to get from leetcode.

Default value is `all`

## Updates

- 2022/11/18: update for website change and use browser cookie
- 2020/01/17: Add Top151 list. [leetcode151][top151]
- 2020/01/16: Rewrite this plugin.
- 2019/08/01: Support custom test input
- 2019/07/28: Support showing frequencies and sorting by columns
- 2019/07/27:
  + Support LeetCode China accounts
  + Support refreshing
- 2019/07/23: Support topics and companies

## FAQ

### I use Ubuntu and get errors when signing in. How can I fix it?

Ubuntu users might see the error message below when signing in.
```text
    raise InitError("Failed to unlock the collection!")
keyring.errors.InitError: Failed to unlock the collection!
```

It's caused by the misconfiguration of python-keyring. One way to fix it is to create a file `~/.local/share/python_keyring/keyringrc.cfg` with the following content:

```ini
[backend]
default-keyring=keyring.backends.Gnome.Keyring
```

### Why can't I test the problem/submit the problem/list the problems?

~~Once you sign in on your browser in LeetCode website, the LeetCode session in
Vim get expired immediatelly. Then you need to sign in again in Vim before
doing other things.~~ (No longer having this problem)

### Why can't I test and submit solutions?

According to issue [#5][#5], **if the email address is not active, then you can
only login and download problems, but cannot test and submit any code.**

### I got some errors like "ModuleNotFoundError: No module named 'keyring.util.escape'"

This solution worked for me:
```shell
pip3 install --upgrade keyrings.alt
```

[top151]: https://github.com/soulmachine/leetcode
[thumbnail]: https://asciinema.org/a/200004.png
[asciicast]: https://asciinema.org/a/200004
[leetcode.vim]: https://github.com/ianding1/leetcode.vim
[leetcode-cli]: https://github.com/skygragon/leetcode-cli
[#5]: https://github.com/ianding1/leetcode.vim/issues/5
[#25]: https://github.com/ianding1/leetcode.vim/issues/25
[user-zhuopro]: https://github.com/zhoupro
