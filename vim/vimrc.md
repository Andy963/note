
.vim/vimrc
```vim
" 设置编码防止中文乱码
set fileencodings=utf-8,gb2312,gb18030,gbk,ucs-bom,cp936,latin1
set nocompatible
filetype off
set rtp+=~/.vim//bundle/Vundle.vim
call vundle#begin()

" 可以在此次安装插件
Plugin 'gmarik/Vundle.vim'

"语法高亮
Plugin 'scrooloose/syntastic'
" pep8风格检查
Plugin 'nvie/vim-flake8'

"超级搜索
Plugin 'kien/ctrlp.vim'

"树形结构文件夹
Bundle 'scrooloose/nerdtree'

"前端用的emmet
Bundle 'mattn/emmet-vim'

"js/css/json格式化
Plugin 'maksimr/vim-jsbeautify'

" 多窗口下最大最小化
Plugin 'szw/vim-maximizer'

" 全局搜索
Plugin 'dkprice/vim-easygrep'

"注释代码
Plugin 'scrooloose/nerdcommenter'

" 浏览当前文件
Plugin 'jlanzarotta/bufexplorer'


"monokai主题
Plugin 'sickill/vim-monokai'


call vundle#end()
filetype plugin indent on


" 设置emmet快捷
let g:user_emmet_expandabbr_key = '<c-tab>'
let g:user_emmet_settings = {'indentation': '    '}
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstall


" 设置多窗口下最大最小化快捷键为F11
nnoremap <silent><F11> :MaximizerToggle<CR>
vnoremap <silent><F11> :MaximizerToggle<CR>gv
inoremap <silent><F11> <C-o>:MaximizerToggle<CR>


" 注释时空一字符
let g:NERDSpaceDelims = 1

" 浏览当前文件列表
nnoremap <silent><F8> :BufExplorer<CR>

"设置使用windows剪贴板
set clipboard=unnamed

" 显示文件夹快捷键
let NERDTreeWinPos='left'
let NERDTreeWinSize=30
map <F2> :NERDTreeToggle<CR>

"设置主题
colorscheme monokai 
"set background=dark
syntax enable


"设置字体大小
set guifont=Consolas:h13

"设置不要交换文件
set noswapfile

"自动缩进
set autoindent
"设置高亮j查找
set incsearch
"设置自动实例括号
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i

" 为gf命令设置扩展名
set suffixesadd +=.py,.rb,.sh
set path=.,/usr/include,,
"设置python文件头
function Header_python()
call setline(1, "#!/usr/bin/env python")
call append(1, "# coding: utf-8 ")
call append(2, "# Create by Andy963 @".strftime('%Y-%m-%d %T', localtime()))
normal G
normal o
normal o
endf
autocmd bufnewfile *.py call Header_python()

```