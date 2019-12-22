def isDriverPresent(name = 'chromedriver'):
    from shutil import which
    if which(name) is None:
        print("\nIt seems 'chromedriver' in ENV. Path is missing.\nSet it in env and rerun file in new window")
        exit()
isDriverPresent()
import os
import time
import re
from datetime import datetime as dt
try:
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
except ModuleNotFoundError:
    mods = ['selenium']
    for m in mods:
        os.system('pip3 install '+ m)
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By


class YTDownloadAutomation(object):
    """docstring for YTDownloadAutomation"""
    def __init__(self):

        self.token = dt.now().strftime("%Y%m%d%H%M%S%f")

        self.dirPath = None
        self.fullPATH = None
        self.prefs = None
        self.browserOptions = None
        self.browser = None

        self.downloaderUrl = "https://en.savefrom.net/"

        self.eachVideosTitles = []
        self.eachVideosUrls = []
        self.downloadLinks = []
        self.completed = []
        
        self.__userChoice()

    def initialize(self,download_path=None):
        if download_path is not None and not os.path.exists(download_path):
            raise Exception("Cannot found the path : " + str(download_path))

        download_path if download_path is not None else self.__setNewDirectory()

        self.fullPATH = download_path if download_path is not None else os.path.join(os.getcwd(),self.dirPath)
        self.prefs = {
        'profile.default_content_setting_values.notifications' : 2 ,
        'profile.default_content_settings.popups' : 0,
        "download.prompt_for_download": False,
        'profile.default_content_setting_values.automatic_downloads': 1,
        'download.default_directory':str(self.fullPATH),
        }
        self.browserOptions = webdriver.ChromeOptions()
        self.browserOptions.add_argument('--start-maximized')
        self.browserOptions.add_experimental_option("prefs", self.prefs)
        self.browser = webdriver.Chrome(options=self.browserOptions)

    def __openUrl(self,url):
        self.browser.execute_script("window.open('"+ url +"');")

    def __userChoice(self):
        ask = ""
        val = None
        while True:
            ask = input("\n1. Start Saved Download (from .html)\n2. Download New \nEnter Choice : ")
            if len(str(ask)) == 1:
                try:
                    val = int(ask)
                    if 0 < val <= 2:
                        break
                    print("Enter respective digit only.")
                except ValueError:
                    print("Enter respective digit only.")
                    continue
            else:
                print("Enter respective digit only.")
        if val == 1:
            filePath = None
            while True:
                filePath = input("Enter path of 'videoLinks.html' :")
                if len(filePath) > 0:
                    break
            if filePath is not None:
                self.initialize(filePath)
                self.__resumeFromHTML()
        if val == 2:
            askUrl = askQual = None
            while True:
                askUrl = input("Enter YT url :")
                askQual = input("Enter quality (360/720) :")
                if len(askQual) > 0 and len(askUrl) > 0:
                    try:
                        askQual = int(askQual)
                        break
                    except ValueError:
                        print("Quality must be a number !")
                        continue
                else:
                    print("Invalid input.")
            if not askQual == askUrl == None:
                # askUrl = "https://www.youtube.com/playlist?list=PLE_gxCZQDh4-55n7ZoY3vgXUla7IMnVY0"
                # askQual = 360
                
                self.initialize()
                self.copyFromYoutube(askUrl,askQual)

    def __openDownloader(self):
        self.__openUrl(self.downloaderUrl)
        rmv = self.browser.window_handles[0]
        self.browser.switch_to.window(rmv)
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def __setNewDirectory(self):
        self.dirPath = "YT_Videos" + str(self.token)
        os.makedirs(self.dirPath)

    def __matchSFN(self, text):
        regex = re.compile(r'^.*?\bsavefrom\b.*?\bnet\b.*?$',flags=re.I)
        return True if regex.search(text) else False

    def __getDownloadLink(self,quality=360):
        self.__openDownloader()
        sfnTab = self.browser.title
        for vlink in self.eachVideosUrls:
            print("Finding input box..")
            while True:
                modal =  self.browser.find_elements_by_css_selector('#modal-container')
                inputField =  self.browser.find_elements_by_css_selector('#sf_url')
                if len(modal) > 0:
                    self.browser.execute_script('var $modalPopUp = document.querySelector("#modal-container");$modalPopUp.parentNode.removeChild($modalPopUp);')
                if len(inputField) > 0:
                    inputField[0].clear()
                    inputField[0].send_keys(vlink)
                    break
            print("Link Pasted..")

            while True:
                submitBtn =  self.browser.find_elements_by_css_selector('#sf_submit')
                if len(inputField) > 0 :
                    submitBtn[0].click();
                    break 
            print("Finding link of {}p quality..".format(str(quality)))
            while True:
                link360p = self.browser.find_elements_by_css_selector('.link-group a[data-quality="'+ str(quality) + '"][data-type="mp4"]')
                linkList = self.browser.find_elements_by_css_selector('.list')
                if len(link360p) > 0 and len(linkList) > 0:
                    self.browser.execute_script("document.getElementsByClassName('list')[0].style.display = 'block'")
                    vdownUrl = link360p[0].get_attribute('href')
                    self.downloadLinks.append(vdownUrl)
                    break

        if len(self.eachVideosUrls) == len(self.downloadLinks):
            self.__writeHTML()
            self.__downloadNewFromHTML()

    def __expand_shadow_element(self,element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def __writeHTML(self):
        name = os.path.join(self.dirPath , "videoLinks.html")
        data = '''
        <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Document</title>
                </head>
                <style>
                    *:not(input) {
                        font-family: sans-serif;
                        font-weight: 500;
                        color: #aaa;
                    }
                    body {
                        background: #000;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 90vh;
                    }
                    .download-links {
                        text-align: center;
                        display: block;
                        color: #aaa;
                        font-family: sans-serif;
                        margin: 16px 0;
                        font-weight: 500;
                        letter-spacing: 1px;
                    }
                    .download-links.done {
                        color: #41d4a4;
                    }
                    #mp4Links {
                        border-right: 1px solid #41d4a4;
                    }
                    #downloaded,
                    #mp4Links {
                        text-align: center;
                        flex: 1 1 50%;
                        max-width: 50%;
                        overflow: auto;
                        height: 100%;
                    }
                </style>
                <body>
                    <div id="mp4Links">
                        <h1>Youtube Links (Grey)</h1>
                    </div>
                    <div id="downloaded">
                        <h1>Downloaded</h1>
                    </div>
                    <script>
                        var completed = '''+ str(list(self.completed)) +'''
                        var linkText = '''+ str(list(self.eachVideosTitles)) +'''
                        var YTLinks = '''+ str(list(self.eachVideosUrls)) +'''
                        var mp4Links = '''+ str(list(self.downloadLinks)) +'''
                        var downloadParent = document.getElementById('downloaded')
                        var mp4Parent = document.getElementById('mp4Links')


                        function changeHrefToYTLink() {
                            for (var i = 0; i < YTLinks.length; i++) {
                                var anchor = document.createElement('a')
                                anchor.setAttribute('class', 'download-links')
                                anchor.setAttribute('href', YTLinks[i])
                                anchor.setAttribute('id', ('download-links' + i.toString()))
                                anchor.setAttribute('data-index', (i.toString()))
                                anchor.innerText = linkText[i]
                                if (completed.indexOf(linkText[i]) !== -1) {
                                    downloadParent.appendChild(anchor)
                                    anchor.classList.add("done")
                                }else{
                                    mp4Parent.appendChild(anchor)
                                }
                            }
                        }
                        changeHrefToYTLink()
                        function changeHrefToMp4(id,index) {
                            document.getElementById(id).setAttribute('href',mp4Links[index]);

                        }
                        function downloaded(id) {
                            document.getElementById(id).classList.add('done')
                        }
                        function renewMp4Links(newArray) {
                            mp4Links = newArray
                        }
                    </script>
                </body>
            </html>
        '''
        with open(name , 'w') as f:
            f.write(data)

    def __getUpdatedHTML(self):
        completed = self.browser.execute_script("return completed")
        YTLinks = self.browser.execute_script("return YTLinks")
        linkText = self.browser.execute_script("return linkText")
        mp4Links = self.browser.execute_script("return mp4Links")
        data = '''
        <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Document</title>
                </head>
                <style>
                    *:not(input) {
                        font-family: sans-serif;
                        font-weight: 500;
                        color: #aaa;
                    }
                    body {
                        background: #000;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 90vh;
                    }
                    .download-links {
                        text-align: center;
                        display: block;
                        color: #aaa;
                        font-family: sans-serif;
                        margin: 16px 0;
                        font-weight: 500;
                        letter-spacing: 1px;
                    }
                    .download-links.done {
                        color: #41d4a4;
                    }
                    #mp4Links {
                        border-right: 1px solid #41d4a4;
                    }
                    #downloaded,
                    #mp4Links {
                        text-align: center;
                        flex: 1 1 50%;
                        max-width: 50%;
                        overflow: auto;
                        height: 100%;
                    }
                </style>
                <body>
                    <div id="mp4Links">
                        <h1>Youtube Links (Grey)</h1>
                    </div>
                    <div id="downloaded">
                        <h1>Downloaded</h1>
                    </div>
                    <script>
                        var completed = '''+ str(list(completed)) +'''
                        var linkText = '''+ str(list(linkText)) +'''
                        var YTLinks = '''+ str(list(YTLinks)) +'''
                        var mp4Links = '''+ str(list(mp4Links)) +'''
                        var downloadParent = document.getElementById('downloaded')
                        var mp4Parent = document.getElementById('mp4Links')


                        function changeHrefToYTLink() {
                            for (var i = 0; i < YTLinks.length; i++) {
                                var anchor = document.createElement('a')
                                anchor.setAttribute('class', 'download-links')
                                anchor.setAttribute('href', YTLinks[i])
                                anchor.setAttribute('id', ('download-links' + i.toString()))
                                anchor.setAttribute('data-index', (i.toString()))
                                anchor.innerText = linkText[i]
                                if (completed.indexOf(linkText[i]) !== -1) {
                                    downloadParent.appendChild(anchor)
                                    anchor.classList.add("done")
                                }else{
                                    mp4Parent.appendChild(anchor)
                                }
                            }
                        }
                        changeHrefToYTLink()
                        function changeHrefToMp4(id,index) {
                            document.getElementById('download-links' + index.toString()).setAttribute('href',mp4Links[index]);
                        }
                        function downloaded(id) {
                            document.getElementById(id).classList.add('done')
                        }
                        function renewMp4Links(newArray) {
                            mp4Links = newArray
                        }
                    </script>
                </body>
            </html>
        '''
        return data
    def __resumeFromHTML(self,quality=360):

        unfinishedYTLinks = [] 

        newMp4Links = []
        activeItems = []
        activeDownloadLists = None
        progressBar = None
        removeBtn = None
        defaultName = "videoplayback.mp4"
        defaultName = os.path.join(self.fullPATH,defaultName)



        # if not os.path.exists(defaultName):
            # raise Exception("'videoplayback.mp4 not found.")
        
        htmlFile = (self.fullPATH.replace("\\","/")) + "/" + "videoLinks.html"
        htmlFileStatic = os.path.join(self.fullPATH, "videoLinks.html")

        if not os.path.exists(htmlFile): return

        htmlFile = "file:///" + htmlFile
        self.browser.get(htmlFile)

        anchors = self.browser.find_elements_by_css_selector('.download-links:not(.done)')

        for i in range(len(anchors)):
            currTab = self.browser.window_handles[0]
            ytlink = anchors[i].get_attribute('href')

            unfinishedYTLinks.append(ytlink)

        self.__openDownloader()

        for vlink in unfinishedYTLinks:
            print("Finding input box..")
            while True:
                modal =  self.browser.find_elements_by_css_selector('#modal-container')
                inputField =  self.browser.find_elements_by_css_selector('#sf_url')
                if len(modal) > 0:
                    self.browser.execute_script('var $modalPopUp = document.querySelector("#modal-container");$modalPopUp.parentNode.removeChild($modalPopUp);')
                if len(inputField) > 0:
                    inputField[0].clear()
                    inputField[0].send_keys(vlink)
                    break
            print("Link Pasted..")

            while True:
                submitBtn =  self.browser.find_elements_by_css_selector('#sf_submit')
                if len(inputField) > 0 :
                    submitBtn[0].click();
                    break 
            print("Finding link of {}p quality..".format(str(quality)))
            while True:
                link360p = self.browser.find_elements_by_css_selector('.link-group a[data-quality="'+ str(quality) + '"][data-type="mp4"]')
                linkList = self.browser.find_elements_by_css_selector('.list')
                if len(link360p) > 0 and len(linkList) > 0:
                    self.browser.execute_script("document.getElementsByClassName('list')[0].style.display = 'block'")
                    vdownUrl = link360p[0].get_attribute('href')
                    newMp4Links.append(vdownUrl)
                    break

        self.browser.get(htmlFile)
        self.browser.execute_script("renewMp4Links("+ str(newMp4Links) + ")")
        anchors = self.browser.find_elements_by_css_selector('.download-links:not(.done)')
        for i in range(len(anchors)):
            currTab = self.browser.window_handles[0]
            curElemId = 'download-links' + str(anchors[i].get_attribute('data-index')) 
            self.browser.execute_script("changeHrefToMp4('" + curElemId + "'," + str(i) +")")
            newName = anchors[i].text
            # self.browser.execute_script("downloaded('download-links"+str(anchors[i].get_attribute('data-index'))+"')")    
            ActionChains(self.browser).key_down(Keys.ALT).click(anchors[i]).key_up(Keys.ALT).perform()
            self.browser.execute_script("downloaded('download-links"+str(anchors[i].get_attribute('data-index'))+"')")
            ActionChains(self.browser).key_down(Keys.CONTROL).click(anchors[i]).key_up(Keys.CONTROL).perform()
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.get("chrome://downloads/")
            self.browser.switch_to.window(self.browser.window_handles[1])

            downloadManager = self.__expand_shadow_element(self.browser.find_element_by_tag_name('downloads-manager'))
            downloadsLists = downloadManager.find_elements_by_css_selector('#downloadsList downloads-item')

            while len(downloadsLists) == 0:
                downloadsLists = downloadManager.find_elements_by_css_selector('#downloadsList downloads-item')

            downloadsLists = self.__expand_shadow_element(downloadsLists[0])
            while True :
                activeDownloadLists = downloadsLists.find_elements_by_css_selector('#content.is-active.show-progress')
                completedDownloads = downloadsLists.find_elements_by_css_selector('#content.is-active.focus-row-active')
                
                if len(activeDownloadLists) > 0:
                    removeBtn = activeDownloadLists[0].find_elements_by_css_selector('#remove')
                    break

            while True:
                progressBar = activeDownloadLists[0].find_elements_by_css_selector('#progress')
                if len(progressBar) > 0:
                    break

            progressValue = int(progressBar[0].get_attribute('value'))
            
            while int(progressValue) < 100:
                progressValue = int(progressBar[0].get_attribute('value'))
                print("Downloading "+ newName +" %d%%\r"%progressValue,end="")

            newNamePath = os.path.join(self.fullPATH,newName)
            time.sleep(0.5)
            print("Renaming the default name.")
            while True:
                try:
                    os.rename(defaultName,newNamePath)
                    print("Successfully Renamed")
                    
                    break
                except FileNotFoundError:
                    pass
            removeBtn[0].click()
            self.browser.close()
            self.browser.switch_to.window(currTab)
            self.browser.execute_script("completed.push('"+ str(newName) + "')")
            data = self.__getUpdatedHTML()
            with open(htmlFileStatic,"w+") as f:
                f.write(data)

    def __downloadNewFromHTML(self):
        # file:///H:/DATA/Python/YT_Videos20191219162517839928/videoLinks.html
        activeItems = []
        activeDownloadLists = None
        progressBar = None
        removeBtn = None
        defaultName = "videoplayback.mp4"
        defaultName = os.path.join(self.fullPATH,defaultName)

        htmlFile = (self.fullPATH.replace("\\","/")) + "/" + "videoLinks.html"
        htmlFileStatic = os.path.join(self.fullPATH, "videoLinks.html")

        if not os.path.exists(htmlFile): return

        htmlFile = "file:///" + htmlFile
        self.browser.get(htmlFile)
        
        anchors = self.browser.find_elements_by_css_selector('.download-links:not(.done)')

        for i in range(len(anchors)):
            currTab = self.browser.window_handles[0]
            curElemId = 'download-links' + str(anchors[i].get_attribute('data-index')) 
            self.browser.execute_script("changeHrefToMp4('" + curElemId + "'," + str(i) +")")
            ActionChains(self.browser).key_down(Keys.ALT).click(anchors[i]).key_up(Keys.ALT).perform()
            self.browser.execute_script("downloaded('download-links"+str(i)+"')")
            ActionChains(self.browser).key_down(Keys.CONTROL).click(anchors[i]).key_up(Keys.CONTROL).perform()
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.get("chrome://downloads/")
            self.browser.switch_to.window(self.browser.window_handles[1])

            downloadManager = self.__expand_shadow_element(self.browser.find_element_by_tag_name('downloads-manager'))
            downloadsLists = downloadManager.find_elements_by_css_selector('#downloadsList downloads-item')

            while len(downloadsLists) == 0:
                downloadsLists = downloadManager.find_elements_by_css_selector('#downloadsList downloads-item')

            downloadsLists = self.__expand_shadow_element(downloadsLists[0])
            while True :
                activeDownloadLists = downloadsLists.find_elements_by_css_selector('#content.is-active.show-progress')
                completedDownloads = downloadsLists.find_elements_by_css_selector('#content.is-active.focus-row-active')
                
                if len(activeDownloadLists) > 0:
                    removeBtn = activeDownloadLists[0].find_elements_by_css_selector('#remove')
                    break

            while True:
                progressBar = activeDownloadLists[0].find_elements_by_css_selector('#progress')
                if len(progressBar) > 0:
                    break

            progressValue = int(progressBar[0].get_attribute('value'))

            while int(progressValue) < 100:
                progressValue = int(progressBar[0].get_attribute('value'))
                print("Downloading "+ self.eachVideosTitles[i] +" %d%%\r"%progressValue,end="")

            newName = self.eachVideosTitles[i]
            newName = os.path.join(self.fullPATH,newName)
            time.sleep(0.5)
            print("Renaming the default name.")

            while True:
                try:
                    os.rename(defaultName,newName)
                    print("Successfully Renamed")
                    self.completed.append(self.eachVideosTitles[i])
                    self.__writeHTML()
                    break
                except FileNotFoundError:
                    pass
            removeBtn[0].click()
            self.browser.close()
            self.browser.switch_to.window(currTab)

    def copyFromYoutube(self,ytUrl,quality=360):
        self.browser.get(ytUrl)
        playlists = []
        
        while True:
            playlists =  self.browser.find_elements_by_css_selector('ytd-playlist-video-renderer > #content > a')
            if len(playlists) > 0:
                break

        for i,each in enumerate(playlists):
            firstTab = self.browser.window_handles[0]
            each.get_attribute('href')

            v_name =str((each.text).split("\n")[1])
            v_name = str(i+1)+ ". " + v_name.replace(" ","-")
            v_name = re.sub(r'[\*\?\|\/\|\"\:\<\>]','',v_name)
            v_name = v_name + ".mp4"
            self.eachVideosTitles.append(v_name)

            ActionChains(self.browser).key_down(Keys.CONTROL).click(each).key_up(Keys.CONTROL).perform()
            self.browser.switch_to.window(self.browser.window_handles[1])
            print("Waiting for 'share' btn")
            while True:
                topLevelBtns =  self.browser.find_elements_by_css_selector('#menu-container #top-level-buttons ytd-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-default.size-default a')
                if len(topLevelBtns) > 0:
                    topLevelBtns[0].click()
                    break
            print("'Share' btn clicked !")

            print("Waiting for pop up")
            while True:
                eachUrl =  self.browser.find_elements_by_css_selector('#share-url')
                if len(eachUrl) > 0 :
                    eachUrl[0].click()
                    self.eachVideosUrls.append(eachUrl[0].get_attribute('value'))
                    break
            print("Url copied !")

            self.browser.close()
            self.browser.switch_to.window(firstTab)

        self.__getDownloadLink(quality)

url = "https://www.youtube.com/playlist?list=PL9fcHFJHtFabrQMoRlfit6kSxXZE5YWU9"
# url = "https://www.youtube.com/playlist?list=PLE_gxCZQDh4-55n7ZoY3vgXUla7IMnVY0"
yt = YTDownloadAutomation()
