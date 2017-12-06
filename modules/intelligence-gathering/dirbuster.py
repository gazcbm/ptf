#!/usr/bin/env python
#####################################
# Installation module for dirbuster
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (@gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update OWASP Dirbuster 1.0 RC1 - a URL brute forcer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/gazcbm/dirbuster-1.0-RC1.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dirbuster"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="dirbuster"

BYPASS_UPDATES="YES"
