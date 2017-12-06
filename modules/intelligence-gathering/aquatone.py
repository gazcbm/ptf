#!/usr/bin/env python
#####################################
# Installation module for aquatone
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Aquatone - Aquatone: http://michenriksen.com/blog/aquatone-tool-for-domain-flyovers"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="aquatone"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, nodejs, nodenpm, rubygems"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git, nodejs, nodenpm, rubygems"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# CREATE LAUNCHER
LAUNCHER="aquatone-scan, aquatone-discovery, aquatone-gather"

# BYPASS UPDATE
BYPASS_UPDATES=""
