#-----------------------------------------------------------------------------------------# 
#                                                                                         #
#    This script creates a Web Design Architecture. See below to know more :              #
#                                                                                         #
#    1. Dictionary's Key is name of directory , whose value is a list of name of          #
#       files in that directory.                                                          #
#                                                                                         #
#    2. If want to create subFolders, then use dictionary in that list, following the     #
#       instruction (1).                                                                  #
#                                                                                         #
#-----------------------------------------------------------------------------------------#

#---------------------------------# 
#                                 #
#    Author : Abhishek Soni       #
#    Format : UTF- 8              #
#    About : CREATE WEB DESIGN    #
#             FOLDER STRUCTURE    #
#                                 #
#---------------------------------#
about='Create Web Design Folder Structure'
print('About : ' + about)
print("Creating...")
import os
from datetime import datetime as dt
import shutil
import sys

# --- Creates File

def createFile(pyVer,fname):
    if pyVer[0] == "2":
        import io
        io.open(fname , "w+" , encoding="utf8")
    else:
        open(fname , "w+" , encoding="utf8")

# --- Writes into File

def writeFile(pyVer , fname , content):
    if pyVer[0] == "2":
        import io
        with io.open(fname , "a") as newFile:
            newFile.write(content)
    else:
        with open(fname , "a") as newFile:
            newFile.write(content)

# --- Different Content to diff file

def writeContent(webFolder,fileData):
    strs = os.walk(webFolder)
    allDirs = os.listdir(webFolder)
    pyVer = sys.version[0:5]
    jsFiles = []
    cssFiles = []

    for root , dirs , f in strs:
        for each in f:
            if each in list(fileData.keys()):
                full_path = os.path.join(root , each)
                print()
                print(full_path)
                print()
                writeFile(pyVer,full_path,fileData[each])
            if ".scss" in each:
                if "_" not in each:
                    mainFile = each
                    mainPath = root
                else:
                    absPath = os.path.join(root , each)
                    fName = each.split(".")
                    relPaths = os.path.join(os.path.relpath(root ,mainPath) , fName[0][1:]).replace("\\" , "/")
                    cnt = '@import "'+ relPaths + '";\n'
                    writeFile(pyVer , os.path.join(mainPath,mainFile) , cnt)
            else:
                if ".css"  in each:
                    absPath = os.path.join(root , each)
                    relPaths = os.path.join(os.path.relpath(root ,webFolder) , each).replace("\\" , "/")
                    cssFiles.append(relPaths)
                elif ".js"  in each:
                    absPath = os.path.join(root , each)
                    relPaths = os.path.join(os.path.relpath(root ,webFolder) , each).replace("\\" , "/")
                    jsFiles.append(relPaths)

    for e in allDirs:
        if e == "index.php":
            cnt = '''<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<meta content="width=device-width ,  initial-scale=1.0" name="viewport">\n\t\t<!-- CSS Libraries -->\n\t\t'''
            for each in cssFiles:
                cnt += '<link href="'+ each + '" rel="stylesheet">\n\t\t'
            cnt += '''\n\t\t<title>\n\t\t\tMy Document\n\t\t</title>\n\t</head>\n\t<body>\n\t<!-- All Javascript/Jqueries -->\n\t\t'''
            for each in jsFiles:
                cnt +='<script src="'+ each + '"></script>\n\t\t'
            cnt += '''\n\t</body>\n</html>'''
            writeFile(pyVer , os.path.join(webFolder , e) , cnt)

# --- Create Project Structure

def create_web_proj(struct):
    global curDir , webFolder
    # infos = str(struct)
    toCopy = "sass.py"
    pyVer = sys.version[0:5]
    mainDir = list(struct.keys())
    token = dt.today().strftime("%d_%m_%Y_%H_%M_%S")
    for k in mainDir:
        if "WEB_PHP" in k:
            withDate = k + "_" + token
            subDir = os.path.join(curDir,withDate)
            curDir = subDir
            os.mkdir(curDir)
            webFolder = curDir
            shutil.copy(toCopy,webFolder)
        else:
            subDir = os.path.join(curDir,k)
            curDir = subDir
            os.mkdir(curDir)
            
        val = struct[k]
        if type(val) != str:
            for each in val:
                if type(each) == str:
                    if "." in each:
                        dist = os.path.join(curDir , each)
                        createFile(pyVer,dist)
                    else:
                        subF = os.path.join(curDir , each)
                        os.mkdir(subF)
                elif type(each) == list:
                    print("Found List ---- " , each)
                elif type(each) == dict:
                    create_web_proj(each)
            if "WEB_PHP" not in k:
                curDir= os.path.join(curDir , "..")
        else:
            print("Other --- " ,val)

def main():
    global curDir , webFolder
    curDir = os.getcwd()
    toCreate = {
    "WEB_PHP": [
                    {
                        "css" : []
                    } ,
                    {
                        "layouts" : [
                                        {
                                            "commons" : ["header.php","footer.php"],
                                        }
                                    ]
                    },
                    "images" ,
                    "pages",
                    {
                        "js" : ["main.js"]
                    } ,
                    "index.php" ,
                    "config.php" ,
                    "connection.php" ,
                    "main.css",
                    
                    {
                    "sass" : ["main.scss" ,
                                {
                                    "abstracts" : ["_functions.scss" , "_mixins.scss" , "_varibales.scss"]
                                } , 
                                {
                                    "base"  : ["_base.scss" , "_animation.scss" , "_keyframes.scss" , "_responsive.scss" , "_typography.scss"]
                                } , 
                                {
                                    "components" : ["_form.scss" , "_input.scss" , "_button.scss" , "_links.scss" , "_messages.scss" , "_others.scss", "_icons.scss"]
                                } ,
                                {
                                    "layouts" : ["_header.scss" , "_footer.scss"]
                                } , 
                                {
                                    "pages" : ["_home.scss"]
                                }]
                    } 
                    ]
    }

    fileContents = {
        "_mixins.scss":'''
            @mixin webkitMaker($prop, $val) {
    @each $prefix in ("-webkit-", "-moz-", "-ms-", "-o-", "") {
        #{$prefix+$prop}: $val;
    }
}
@mixin transit($dur) {
    @include webkitMaker(transition, $dur);
}
@mixin size($width, $height: $width) {
    width: $width;
    height: $height;
}
@mixin posCenter($w: 100%, $h: $w) {
    position: absolute;
    top: 50%;
    left: 50%;
    @include size($w, $h);
    @include webkitMaker(transform, translate(-50%, -50%));
}
@mixin posCustom($w: 100%, $h: $w, $T: 0, $L: 0) {
    position: absolute;
    top: $T;
    left: $L;
    @include size($w, $h);
}
@mixin posCustomBR($w: 100%, $h: $w, $B: 0, $R: 0) {
    position: absolute;
    bottom: $B;
    right: $R;
    @include size($w, $h);
}
@mixin transF($val) {
    @include webkitMaker(transform, #{$val});
}
@mixin center($mY: 0) {
    margin: $mY auto;
    display: table;
}
@mixin gradient-bg($clr1, $clr2: $trans, $endClr1: 0%, $endClr2: 100%, $rot: 45deg) {
    background: Grad($clr1, $clr2, $endClr1, $endClr2, $rot);
}
// Horizontal gradient, from left to right
@mixin gradient-x($start-color: #000, $end-color: #fff, $start-percent: 0%, $end-percent: 100%,$x:'to right') {
    background: Grad($clr1, $clr2, $endClr1, $endClr2, $rot);
    background: linear-gradient(#{$x}, $start-color $start-percent, $end-color $end-percent);
}

// Vertical gradient, from top to bottom
@mixin gradient-y($start-color: #000, $end-color: #fff, $start-percent: 0%, $end-percent: 100%) {
    background: linear-gradient(to bottom, $start-color $start-percent, $end-color $end-percent);
}

@mixin gradient-radial($inner-color: #000, $outer-color: #fff) {
    background: radial-gradient(circle, $inner-color, $outer-color);
    background-repeat: no-repeat; 
}
@mixin gradient-striped($color: rgba(#000, 0.15), $angle: 45deg) {
    background: linear-gradient(
        $angle,
        $color 25%,
        transparent 25%, 
        transparent 50%,
        $color 50%,
        $color 75%,
        transparent 75%,
        transparent
    ); 
}
@mixin setFont($name: inherit, $size: inherit, $wght: inherit) {
    font-family: $name;
    font-size: $size;
    font-weight: $wght;
}
@mixin boxShad($x: 0, $y: 0, $blur: 0, $spread: 0, $clr: #000) {
    @include webkitMaker(box-shadow, #{$x $y $blur $spread $clr});
}
@mixin keyFrames($name) {
    @-webkit-keyframes #{$name} {
        @content;
    }
    @-moz-keyframes #{$name} {
        @content;
    }
    @-ms-keyframes #{$name} {
        @content;
    }
    @-o-keyframes #{$name} {
        @content;
    }
    @keyframes #{$name} {
        @content;
    }
}
@mixin anim($name, $dur: 1s, $direction: normal, $func: ease, $mode: infinite) {
    @include webkitMaker(animation, #{$name $dur $direction $func $mode});
}
@mixin hoverFocus {
    &:hover,
    &:focus {
        @content;
    }
}

@mixin setBGImg($path, $size: cover, $x: center, $y: center) {
    background-image: url(#{$imgPath+$path});
    background-size: $size;
    background-position: $x $y;
    background-repeat: no-repeat;
}



@mixin classForBP($bpName) {
    @if ($bpName == "") {
        @content;
    }
    @if ($bpName == "-xxs") {
        @media only screen and (max-width: 359.98px) {
            @content;
        }
    }
    @if ($bpName == "-xs") {
        // Extra small devices (portrait phones, less than 576px)
        @media only screen and (min-width: 360px) and (max-width: 575.98px) {
            @content;
        }
    }
    @if ($bpName == "-sm") {
        // Small devices (landscape phones, 576px and up)
        @media only screen and (min-width: 576px) and (max-width: 767.98px) {
            @content;
        }
    }
    @if ($bpName == "-md") {
        // Medium devices (tablets, 768px and up)
        @media only screen and (min-width: 768px) and (max-width: 991.98px) {
            @content;
        }
    }
    @if ($bpName == "-lg") {
        // Large devices (desktops, 992px and up)
        @media only screen and (min-width: 992px) and (max-width: 1199.98px) {
            @content;
        }
    }
    @if ($bpName == "-xl") {
        // Extra large devices (large desktops, 1200px and up)
        @media only screen and (min-width: 1200px) {
            @content;
        }
    }
    // @if ($bpName == "xl") {
    //     // Large devices (desktops, 992px and up)
    //     @media only screen and (min-width: 992px) and (max-width: 1199.98px) {
    //         @content;
    //     }
    // }
    // @if ($bpName == "xl") {
    //     // Large devices (desktops, 992px and up)
    //     @media only screen and (min-width: 992px) and (max-width: 1199.98px) {
    //         @content;
    //     }
    // }
}

@mixin gradTxt($grad,$textClr:$trans) {
    color:$textClr;
    background: $grad;
    @include webkitMaker(background-clip,text);
}
        ''',
        "_varibales.scss":'''
        @function Grad($clr1, $clr2, $endClr1: 0%, $endClr2: 100%, $rot: 45deg) {
    @return #{"linear-gradient(" + $rot + "," + $clr1 + " " + $endClr1 + "," + $clr2 + " " + $endClr2 + ")"};
}


$primary: #666;
$secondary: #666;
$info: #17c0eb;
$error: #ff3838;
$danger: #ff9f1a;

$black: #000;
$white: #fff;

$dark: #19191d;

$trans: transparent;

$colors: (
    "primary": $primary,
    "secondary": $secondary,
    "info": $info,
    "error": $error,
    "danger": $danger,
    "black": $black,
    "white": $white,
    "dark": $dark,
);

$breakpoints-class: ("", "-xxs", "-xs", "-sm", "-md", "-lg", "-xl");
$spacer: 1rem !default;
$spacers: () !default;
$spacers: map-merge(
    (
        0: 0,
        1: (
            $spacer * 0.25
        ),
        2: (
            $spacer * 0.5
        ),
        3: $spacer,
        4: (
            $spacer * 1.5
        ),
        5: (
            $spacer * 3
        )
    ),
    $spacers
);
$imgPath: "./images/";
''',

"_base.scss":'''*,
*:before,
*:after {
    box-sizing: inherit;
    margin: 0;
    padding: 0;
}
*:focus,
*:hover {
    outline: none;
}
body {
    color: $dark;
    line-height: 1.5;
    box-sizing: border-box;
    min-width: 320px;
    overflow-x: hidden;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    color: $dark;
    padding: 0;
    line-height: 1.5;
    margin-bottom: 1rem;
}
p {
    color: $dark;
}

p,
a,
span,
small {
    line-height: 1.5;
}
p,
a,
span,
small,
button,
input,
textarea,
label {
    padding: 0;
}
a {
    display: inline-block;
    text-decoration: none;
    &:hover {
        text-decoration: none;
    }
}
button {
    cursor: pointer;
    background: none;
    border: none;
    &:focus,
    &:hover {
        outline: none;
    }
}
a,
button,
input,
textarea {
    @include transit(0.25s);
}
input,
textarea {
    border: none;
    @include hoverFocus {
        outline: none;
    }
}
ul,
ol {
    list-style: none;
    margin: 0;
    padding: 0;
}
@include setChildCmnt("custom classes starts");

@each $className, $clr in $colors {
    @if (not str-index($string: $className, $substring: "grad-")) {
        #{".text-" + $className} {
            color: $clr !important;
        }
    }
}
@each $className, $clr in $colors {
    #{".bg-" + $className} {
        background: $clr !important;
    }
}
@each $bpName in $breakpoints-class {
    @include classForBP($bpName) {
        @each $num, $val in $spacers {
            #{".p" + $bpName + "-" + $num} {
                padding: #{$val + " !important"};
            }
        }
    }
}
''',

"_responsive.scss":'''@media only screen and (max-width: 359.98px) {
    //
}
// Extra small devices (portrait phones, less than 576px)
@media only screen and (min-width: 360px) and (max-width: 575.98px) {
    //
}

// Small devices (landscape phones, 576px and up)
@media only screen and (min-width: 576px) and (max-width: 767.98px) {
    //
}

// Medium devices (tablets, 768px and up)
@media only screen and (min-width: 768px) and (max-width: 991.98px) {
    //
}

// Large devices (desktops, 992px and up)
@media only screen and (min-width: 992px) and (max-width: 1199.98px) {
    //
}

// Extra large devices (large desktops, 1200px and up)
@media only screen and (min-width: 1200px) and (max-width: 1365.98px) {
    //
}
@media only screen and (min-width: 1366px) and (max-width: 1919.98px) {
    //
}
@media only screen and (min-width: 1920px) and (max-width: 1919.98px) {
    //
}
''',

"main.scss":'''@function capitalize($string) {
    @return to-upper-case(str-slice($string, 1, 1)) + str-slice($string, 2);
}
@function str-ucwords($string) {
    $progress: $string;
    $result: "";

    $running: true;

    @while $running {
        $index: str-index($progress, " ");
        @if $index {
            $result: $result + capitalize(str-slice($progress, 1, $index));
            $progress: str-slice($progress, ($index + 1));
        } @else {
            $running: false;
        }
    }

    @return capitalize($result) + capitalize($progress);
}
@mixin setMainCmnt($msg) {
    /*#{'||  ======================  '+ str-ucwords($msg) +'  ======================  ||'}*/
}
@mixin setChildCmnt($msg) {
    /*#{'||  ----  '+ str-ucwords($msg) +'  ----  ||'}*/
}


''',
"connection.php":'''<?php
include_once "config.php";
try {
    $pdoconn = new PDO("mysql:host=$host;dbname=$database", $user, $pwd, array(PDO::ATTR_PERSISTENT => true));
    //Describe how to handle error. Here, throws exception.
    $pdoconn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $error) {
    echo "Error in connection :" . $error;
}''',
"config.php":'''<?php
$host = "localhost";
$user = "root";
$pwd = "";
$database = "db_name";
?>''',
    }
    create_web_proj(toCreate)
    writeContent(webFolder,fileContents)

if __name__=="__main__":
    main()
