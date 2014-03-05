#Copyright 2011-2012 Mitchell Jon Stanton-Cook Licensed under the
#Educational Community License, Version 2.0 (the "License"); you may
#not use this file except in compliance with the License. You may
#obtain a copy of the License at
#
#http://www.osedu.org/licenses/ECL-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an "AS IS"
#BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#or implied. See the License for the specific language governing 
#permissions and limitations under the License. 

"""
The Banzai Pipeline controller

This code was created by Mitchell Stanton-Cook under the employment of Dr 
Scott Beatson. DO NOT REMOVE THIS MESSAGE.
"""

__author__  = "Mitchell Stanton-Cook"
__licence__ = "ECL-2.0"
__version__ = "0.1"
__email__   = "m.stantoncook@gmail.com"
epi = "Licence: "+ __licence__ +  " by " + __author__ + " <" + __email__ + ">"


import sys
import os
from fabric.api   import *
from ConfigParser import SafeConfigParser

# For debugging of Fabric get/put etc
#import logging
#logging.basicConfig()
#logging.getLogger('ssh.transport').setLevel(logging.INFO)


def getConfig(cfg_file_path=None):
    """
    Get/return the Banzai controller's config

    Assumes a config file in the following format:

    [hpc]
    hosts = uqmstan1@barrine.hpcu.uq.edu.au:22 mscook@lychee.md.smms.uq.edu.au:2023

    [local]
    hosts = mscook@smms-edmund.biosci.uq.edu.au:22

    [webserver]
    hosts = mscook@smms-steel.biosci.uq.edu.au:22


    :param cfg_file_path: [default = None] The full path and file name to the 
                          controllers config file as a string
    :type cfg_file_path: string

    :rtype: Fabric's env.hosts & env.roledefs
    """
    parser = SafeConfigParser()
    parser.read('data/Banzai-controller.cfg')
    # HPC
    hpc_hosts = parser.get('hpc', 'hosts').split(' ')
    env.roledefs['hpc'] = hpc_hosts
    env.roledefs['hpc_default'] = [hpc_hosts[0]]
    # Web Servers
    web_hosts = parser.get('webserver', 'hosts').split(' ')
    env.roledefs['web'] = web_hosts
    env.roledefs['web_default'] = [web_hosts[0]]
    # Do local
    loc_hosts = parser.get('local', 'hosts').split(' ')
    env.roledefs['local'] = loc_hosts
    env.roledefs['local_default'] = [loc_hosts[0]]
    env.hosts = hpc_hosts + web_hosts + loc_hosts
    return env.hosts, env.roledefs


@task
def getBanzairc(project_base, server=None):
    """
    Saves the banzairc in project_base on the hpc resource to the $CWD
    """
    project_base = os.path.expanduser(project_base)
    if project_base[-1] != '/':
        project_base = project_base+'/'
    project = project_base.split('/')[-2]
    env.hosts, env.roledefs = getConfig()
    if server is None:
        server = env.roledefs['hpc_default'][0]
    with settings(host_string=server):
        get(project_base+'Banzairc', project+"/%(basename)s")

@task
def putBanzairc(project_base, server=None):
    """
    Puts the $PROJECT/banzairc into project_base on the hpc resource
    """
    project_base = os.path.expanduser(project_base)
    if project_base[-1] != '/':
        project_base = project_base+'/'
    project = project_base.split('/')[-2]
    env.hosts, env.roledefs = getConfig()
    if server is None:
        server = env.roledefs['hpc_default'][0]
    with settings(host_string=server):
        put(project+"/Banzairc", project_base+'Banzairc')




@task
def putReads(local_reads_dir, remote_reads_dest, server=None):
    """
    Puts reads onto the default hpc resource
    """
    env.hosts, env.roledefs = getConfig()
    if server is None:
        host_string = env.roledefs['hpc_default']
    with settings(host_string=server):
        run('ls ~/')

@task
def runQC(project_base, options=None, server=None):
    """
    Initiates a QC run on the default hpc resource
    """
    env.hosts, env.roledefs = getConfig()
    cmd = 'fab runQC:'+project_base
    if options is not None:
        base = base+options
    if server is None:
        server = env.roledefs['hpc_default'][0]
    with settings(host_string=server):
        run(cmd)







@task
def getAss():
    """
    Puts reads onto a hpc resource
    """
    pass

@task
def getMap():
    """
    Puts reads onto a hpc resource
    """
    pass

@task
def getOrdering():
    """
    Puts reads onto a hpc resource
    """
    pass

@task
def getAnn():
    """
    Puts reads onto a hpc resource
    """
    pass



