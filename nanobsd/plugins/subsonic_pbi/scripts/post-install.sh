#!/bin/sh

SUBSONIC_HOME=/usr/pbi/subsonic-`uname -m`

# New strategy, put syncdb first to see if it works here
env -i ${SUBSONIC_HOME}/bin/python ${SUBSONIC_HOME}/subsonicUI/manage.py syncdb --migrate --noinput

echo libz.so.4 libz.so.5 > /etc/libmap.conf
echo libz.so.4 libz.so.5 > ${SUBSONIC_HOME}/etc/libmap.conf

mkdir -p ${SUBSONIC_HOME}/etc/subsonic/home
mkdir /var/subsonic /var/music /var/playlists

chown -R www:www /var/subsonic
chown -R www:www /var/music
chown -R www:www /var/playlists
chown www:www ${SUBSONIC_HOME}/apache-tomcat-6.0/webapps/subsonic.war

echo "tomcat60_java_opts="-Djava.awt.headless=true -Djava.net.preferIPv4Stack=true" >> /etc/rc.conf

cp ${SUBSONIC_HOME}/etc/rc.d/ffserver /usr/local/etc/rc.d/
cp ${SUBSONIC_HOME}/etc/rc.d/ffserver /etc/rc.d/
cp ${SUBSONIC_HOME}/etc/rc.d/tomcat6 /usr/local/etc/rc.d/

ln -s ${SUBSONIC_HOME}/bin/lame /var/subsonic/transcode/

mkdir -p ${SUBSONIC_HOME}/MEDIA
chown www:www ${SUBSONIC_HOME}/MEDIA
chmod 775 ${SUBSONIC_HOME}/MEDIA


# The following 2 sed commands let Subsonic determine the Jail IP address and add it to the JAVA_OPTS used to start Subsonic

# William suggests just using 0.0.0.0
JAIL_IP=`ifconfig | grep -E 'inet.[0-9]' | grep -v '127.0.0.1' | awk '{ print $2}'` 

# Check if our hostname or ip address changed. Also make sure another plugin hasn't added it.
#if [ `grep -c $JAIL_IP /etc/hosts` -eq 0 ]
    echo $JAIL_IP"	"`hostname` >> /etc/hosts
#fi

echo 'subsonic_flags=""' > ${SUBSONIC_HOME}/etc/rc.conf
echo 'subsonic_flags=""' > /etc/rc.conf
