:set number
:set autoindent
:set smarttab
:set mouse=a
:set tabstop=4
:set shiftwidth=4
:set softtabstop=4
:set encoding=UTF-8

call plug#begin()

Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/tc50cal/vim-terminal'
Plug 'https://github.com/mg979/vim-visual-multi'
Plug 'https://github.com/preservim/tagbar'
Plug 'https://github.com/neoclide/coc.nvim'
Plug 'https://github.com/github/copilot.vim'
Plug 'vimwiki/vimwiki'
Plug 'nvim-orgmode/orgmode'
Plug 'https://github.com/mattn/calendar-vim'
Plug 'https://github.com/ryanoasis/vim-devicons'
Plug 'https://github.com/tools-life/taskwiki'
Plug 'https://github.com/powerman/vim-plugin-AnsiEsc'
" Plug 'https://github.com/majutsushi/tagbar'
" Plug 'https://github.com/farseer90718/vim-taskwarrior'

call plug#end()

nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="~"
let g:VM_mouse_mappings = 1

nmap <F8> :TagbarToggle<CR>

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm() : "\<CR>"

