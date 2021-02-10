imperial_materials_download() {
        cd ~/imperial/imperial-computing-materials-downloader
        python3 materials-downloader.py "$@"
        cd
}

alias impmat="imperial_materials_download"
