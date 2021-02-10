imperial_materials_download() {
        cd ~/imperial/imperial-computing-materials-downloader # path to your repository
        python3 materials-downloader.py "$@"                  # call to script
        cd -                                                  # returning to working directory
}

alias impmat="imperial_materials_download"
