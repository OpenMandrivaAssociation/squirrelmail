%define mod_conf 73_squirrelmail.conf

# helps to find new languages
%define _unpackaged_files_terminate_build 0

%define basedir /var/www/squirrelmail
%define varlibdir /var/lib/squirrelmail
%define prefsdir %{varlibdir}/prefs
%define varspooldir /var/spool/squirrelmail
%define attdir %{varspooldir}/attach
%define etcdir /etc/squirrelmail
%define crondir /etc/cron.daily
# Plugin config files
%define pluginetc %{etcdir}/plugins

%define locale_stamp 20070106

Summary:	Squirrelmail is a webmail client for PHP4
Name:		squirrelmail
Version:	1.4.10a
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://www.squirrelmail.org/
Source0:	http://prdownloads.sf.net/squirrelmail/%{name}-%{version}.tar.gz
Source1:	http://prdownloads.sf.net/squirrelmail/all_locales-1.4.9-%{locale_stamp}.tar.gz
Source2:	squirrelmail-RPM.readme
Source3:	http://www.squirrelmail.org/plugins/address_add-2.1-1.4.0.tar.bz2
Source4:	http://www.squirrelmail.org/plugins/block_sender.2.02-1.4.0.tar.bz2
Source5:	http://www.squirrelmail.org/plugins/login_image-0.2.tar.bz2
Source6:	http://www.squirrelmail.org/plugins/secure_login-1.2-1.2.8.tar.bz2
Source7:	http://www.squirrelmail.org/plugins/compatibility-2.0.4.tar.bz2
Source8:	http://www.squirrelmail.org/plugins/change_pass-2.7-1.4.x.tar.bz2
Source9:	http://www.squirrelmail.org/plugins/quota_usage-1.3-1.2.7.tar.bz2
# http://sourceforge.net/tracker/index.php?func=detail&aid=1255733&group_id=311&atid=300311
Source10:	http://www.squirrelmail.org/plugins/change_ldappass-1.9.1.tar.bz2
Source11:	http://www.squirrelmail.org/plugins/avelsieve-1.0.1.tar.bz2
Source12:	http://www.squirrelmail.org/plugins/windows-1.6-1.4.tar.bz2
Source13:	http://www.squirrelmail.org/plugins/folder_sizes-1.5-1.4.0.tar.bz2
Source14:	http://www.squirrelmail.org/plugins/archive_mail.1.2-1.4.2.tar.bz2
Source15:	http://www.squirrelmail.org/plugins/empty_folders-1.2-1.2.tar.bz2
Source16:	http://www.squirrelmail.org/plugins/abook_import_export-1.0-1.4.4.tar.bz2
Source17:	http://www.squirrelmail.org/plugins/ldifimport-1.4-1.2.x.tar.bz2
Source18:	http://www.squirrelmail.org/plugins/username-2.3-1.0.0.tar.bz2
Source19:	http://www.squirrelmail.org/plugins/bookmarks-2.0.3-1.4.1.tar.bz2
Source20:	http://www.squirrelmail.org/plugins/select_range-3.5.tar.bz2
Source21:	http://www.squirrelmail.org/plugins/rewrap.1.2-1.4.0.tar.bz2
Source22:	http://www.squirrelmail.org/spam_buttons-1.0-1.4.tar.bz2
# http://sourceforge.net/projects/php-sa-mysql
Source23:	http://prdownloads.sourceforge.net/php-sa-mysql/SquirrelSAP105.tar.bz2
Source24:	http://squirrelmail.org/plugins/junkfolder-1.0.tar.bz2
Source25:	conf.pl
# branding :)
Source100:	logoMDA-CS.png
Patch0:		squirrelmail-1.4.8-get_branded.diff
Patch1:		squirrelmail-1.4.2-config.php.patch
Patch2:		squirrelmail-1.4.5-change_pass_syntax.diff
Patch5:		login_image-position.diff
Patch6:		secure_login-stayinssl.patch
Patch7:		squirrelmail-1.4.1-default_folder_prefix.patch
Patch8:		squirrelmail-select_range.diff
Patch10:	squirrelmail-1.4.6-ldappass.diff
Patch11:	squirrelmail-1.4.3a-avelsieve-0.9.11.patch
Patch12:	squirrelmail-1.4.2-sqspell.patch
Patch13:	squirrelmail-1.4.2-filters.patch
Patch14:	squirrelmail-1.4.6-aspell.diff
Patch17:	squirrelmail-1.4.4-log_failed_login_attempts.diff
Patch18:	squirrelmail-sieve_syntax_error.patch
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):  apache-conf >= 2.0.54
Requires(pre):  apache-mpm >= 2.0.54
Requires:	apache-conf >= 2.0.54
Requires:	apache-mpm >= 2.0.54
Requires:	apache-mod_php
Requires:	sendmail-command
Requires:	aspell
Requires:	bash
Requires:	perl
Requires:	php-imap
Requires:	php-ldap
Requires:	poppassd-ceti
Requires:	tmpwatch >= 2.8
# We use ccp to upgrade our config file when possible
Requires(post):	ccp >= 0.4.0
BuildRequires:	dos2unix
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
SquirrelMail is a standards-based webmail package written in PHP4. It
includes built-in pure PHP support for the IMAP and SMTP protocols, and
all pages render in pure HTML 4.0 (with no Javascript) for maximum
compatibility across browsers.  It has very few requirements and is very
easy to configure and install. SquirrelMail has all the functionality
you would want from an email client, including strong MIME support,
address books, and folder manipulation.

%package	poutils
Summary:	Some development tools for SquirrelMail
Group:		System/Servers
Requires:	%{name} = %{version}

%description	poutils
This package includes some development tools for squirrelmail
i18n, including the main po file and some compilation scripts.

%package	cyrus
Summary:	Cyrus meta package for SquirrelMail
Group:		System/Servers
Requires:	%{name} = %{version}
Requires:	sasl-plug-login
Requires:	sasl-plug-plain
Requires:	cyrus-imapd
Requires:	cyrus-imapd-utils
Requires:	cyrus-sasl

%description	cyrus
Cyrus meta package for SquirrelMail.

%package	ar
Summary:	Arabic language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ar
Requires:	%{name} = %{version}

%description	ar
This add-on package provides Arabic translation for
Squirrelmail.

%package	bg
Summary:	Bulgarian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-bg
Requires:	%{name} = %{version}

%description	bg
This add-on package provides Bulgarian translation for
Squirrelmail.

%package	bn
Summary:	Bengali language files for SquirrelMail
Group:		System/Servers
Requires:	locales-bn
Requires:	%{name} = %{version}

%description	bn
This add-on package provides Bengali translation for
Squirrelmail.

%package	ca
Summary:	Catalan language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ca
Requires:	%{name} = %{version}

%description	ca
This add-on package provides Catalan translation for
Squirrelmail.

%package	cs
Summary:	Czech language files for SquirrelMail
Group:		System/Servers
Requires:	locales-cs
Requires:	%{name} = %{version}

%description	cs
This add-on package provides Czech translation for
Squirrelmail.

%package	cy
Summary:	Welsh language files for SquirrelMail
Group:		System/Servers
Requires:	locales-cy
Requires:	%{name} = %{version}

%description	cy
This add-on package provides Welsh translation for
Squirrelmail.

%package	da
Summary:	Danish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-da
Requires:	%{name} = %{version}

%description	da
This add-on package provides Danish translation for
Squirrelmail.

%package	de
Summary:	German language files for SquirrelMail
Group:		System/Servers
Requires:	locales-de
Requires:	%{name} = %{version}

%description	de
This add-on package provides German translation for
Squirrelmail.

%package	el
Summary:	Greek language files for SquirrelMail
Group:		System/Servers
Requires:	locales-el
Requires:	%{name} = %{version}

%description	el
This add-on package provides Greek translation for
Squirrelmail.

%package	en
Summary:	British language files for SquirrelMail
Group:		System/Servers
Requires:	locales-en
Requires:	%{name} = %{version}

%description	en
This add-on package provides British translation for
Squirrelmail.

%package	es
Summary:	Spanish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-es
Requires:	%{name} = %{version}

%description	es
This add-on package provides Spanish translation for
Squirrelmail.

%package	et
Summary:	Estonian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-et
Requires:	%{name} = %{version}

%description	et
This add-on package provides Estonian translation for
Squirrelmail.

%package	eu
Summary:	Basque language files for SquirrelMail
Group:		System/Servers
Requires:	locales-eu
Requires:	%{name} = %{version}

%description	eu
This add-on package provides Basque translation for
Squirrelmail.

%package	fa
Summary:	Farsi language files for SquirrelMail
Group:		System/Servers
Requires:	locales-fa
Requires:	%{name} = %{version}

%description	fa
This add-on package provides Farsi translation for
Squirrelmail.

%package	fi
Summary:	Finnish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-fi
Requires:	%{name} = %{version}

%description	fi
This add-on package provides Finnish translation for
Squirrelmail.

%package	fo
Summary:	Faroese language files for SquirrelMail
Group:		System/Servers
Requires:	locales-fo
Requires:	%{name} = %{version}

%description	fo
This add-on package provides Faroese translation for
Squirrelmail.

%package	fr
Summary:	French language files for SquirrelMail
Group:		System/Servers
Requires:	locales-fr
Requires:	%{name} = %{version}

%description	fr
This add-on package provides French translation for
Squirrelmail.

%package	he
Summary:	Hebrew language files for SquirrelMail
Group:		System/Servers
Requires:	locales-he
Requires:	%{name} = %{version}

%description	he
This add-on package provides Hebrew translation for
Squirrelmail.

%package	hr
Summary:	Croatian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-hr
Requires:	%{name} = %{version}

%description	hr
This add-on package provides Croatian translation for
Squirrelmail.

%package	hu
Summary:	Hungarian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-hu
Requires:	%{name} = %{version}

%description	hu
This add-on package provides Hungarian translation for
Squirrelmail.

%package	id
Summary:	Indonesian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-id
Requires:	%{name} = %{version}

%description	id
This add-on package provides Indonesian translation for
Squirrelmail.

%package	is
Summary:	Icelandic language files for SquirrelMail
Group:		System/Servers
Requires:	locales-is
Requires:	%{name} = %{version}

%description	is
This add-on package provides Icelandic translation for
Squirrelmail.

%package	it
Summary:	Italian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-it
Requires:	%{name} = %{version}

%description	it
This add-on package provides Italian translation for
Squirrelmail.

%package	ja
Summary:	Japanese language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ja
Requires:	%{name} = %{version}

%description	ja
This add-on package provides Japanese translation for
Squirrelmail.

%package	ko
Summary:	Korean language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ko
Requires:	%{name} = %{version}

%description	ko
This add-on package provides Korean translation for
Squirrelmail.

%package	lt
Summary:	Lithuanian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-lt
Requires:	%{name} = %{version}

%description	lt
This add-on package provides Lithuanian translation for
Squirrelmail.

%package	ms
Summary:	Bahasa Melayu language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ms
Requires:	%{name} = %{version}

%description	ms
This add-on package provides Bahasa Melayu translation for
Squirrelmail.

%package	nb
Summary:	Norwegian Bokmål language files for SquirrelMail
Group:		System/Servers
Requires:	locales-nb
Requires:	%{name} = %{version}
Obsoletes:	%{name}-nb_NO

%description	nb
This add-on package provides Norwegian Bokmal translation for
Squirrelmail.

%package	nl
Summary:	Dutch language files for SquirrelMail
Group:		System/Servers
Requires:	locales-nl
Requires:	%{name} = %{version}

%description	nl
This add-on package provides Dutch translation for
Squirrelmail.

%package	nn
Summary:	Norwegian Nynorsk language files for SquirrelMail
Group:		System/Servers
Requires:	locales-nn
Requires:	%{name} = %{version}
Obsoletes:	%{name}-nn_NO

%description	nn
This add-on package provides Norwegian Nynorsk translation for
Squirrelmail.

%package	pl
Summary:	Polish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-pl
Requires:	%{name} = %{version}

%description	pl
This add-on package provides Polish translation for
Squirrelmail.

%package	pt
Summary:	Portuguese and Brazilian Portuguese language files for SquirrelMail
Group:		System/Servers
Requires:	locales-pt
Requires:	%{name} = %{version}
Provides:	%{name}-pt_BR = %{version}
Obsoletes:	%{name}-pt_BR

%description	pt
This add-on package provides Portuguese and Brazilian Portuguese translation
for Squirrelmail.

#%package	pt_BR
#Summary:	Brazilian Portuguese language files for SquirrelMail
#Group:		System/Servers
#Requires:	locales-pt_BR
#Requires:	%{name} = %{version}

#%description	pt_BR
#This add-on package provides Brazilian Portuguese translation for
#Squirrelmail.

%package	ro
Summary:	Romanian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ro
Requires:	%{name} = %{version}

%description	ro
This add-on package provides Romanian translation for
Squirrelmail.

%package	ru
Summary:	Russian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ru
Requires:	%{name} = %{version}

%description	ru
This add-on package provides Russian translation for
Squirrelmail.

%package	sk
Summary:	Slovak language files for SquirrelMail
Group:		System/Servers
Requires:	locales-sk
Requires:	%{name} = %{version}

%description	sk
This add-on package provides Slovak translation for
Squirrelmail.

%package	sl
Summary:	Slovenian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-sl
Requires:	%{name} = %{version}

%description	sl
This add-on package provides Slovenian translation for
Squirrelmail.

%package	sr
Summary:	Serbian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-sr
Requires:	%{name} = %{version}

%description	sr
This add-on package provides Serbian translation for
Squirrelmail.

%package	sv
Summary:	Swedish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-sv
Requires:	%{name} = %{version}

%description	sv
This add-on package provides Swedish translation for
Squirrelmail.

%package	th
Summary:	Thai language files for SquirrelMail
Group:		System/Servers
Requires:	locales-th
Requires:	%{name} = %{version}

%description	th
This add-on package provides Thai translation for
Squirrelmail.

%package	tl
Summary:	Filipino language files for SquirrelMail
Group:		System/Servers
Requires:	locales-tl
Requires:	%{name} = %{version}

%description	tl
This add-on package provides Filipino translation for
Squirrelmail.

%package	tr
Summary:	Turkish language files for SquirrelMail
Group:		System/Servers
Requires:	locales-tr
Requires:	%{name} = %{version}

%description	tr
This add-on package provides Turkish translation for
Squirrelmail.

%package	ug
Summary:	Uighur language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ug
Requires:	%{name} = %{version}

%description	ug
This add-on package provides Uighur translation for
Squirrelmail.

%package	uk
Summary:	Ukrainian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-uk
Requires:	%{name} = %{version}

%description	uk
This add-on package provides Ukrainian translation for
Squirrelmail.

%package	vi
Summary:	Vietnamese language files for SquirrelMail
Group:		System/Servers
Requires:	locales-vi
Requires:	%{name} = %{version}

%description	vi
This add-on package provides Vietnamese translation for
Squirrelmail.

%package	zh_CN
Summary:	Chinese Simplified language files for SquirrelMail
Group:		System/Servers
Requires:	locales-zh
Requires:	%{name} = %{version}

%description	zh_CN
This add-on package provides Chinese Simplified translation for
Squirrelmail.

%package	zh_TW
Summary:	Chinese Traditional language files for SquirrelMail
Group:		System/Servers
Requires:	locales-zh
Requires:	%{name} = %{version}

%description	zh_TW
This add-on package provides Chinese Traditional translation for
Squirrelmail.

%package	ka
Summary:	Georgian language files for SquirrelMail
Group:		System/Servers
Requires:	locales-ka
Requires:	%{name} = %{version}

%description	ka
This add-on package provides Georgian translation for
Squirrelmail.

%prep

%setup -q -a1
%patch0 -p0
%patch7 -p1
%patch8 -p1
%patch12 -p1
%patch14 -p0
%patch17 -p0

rm -f plugins/make_archive.pl

# branding :)
install -m0644 %{SOURCE100} images/mandriva.png

# hard code the path to the core config files

find . -type f|xargs perl -pi -e "s|SM_PATH \. \'config/config\.php\'|\'%{etcdir}/config\.php\'|g; \
    s|SM_PATH \. \"config/config\.php\"|\'%{etcdir}/config\.php\'|g; \
    s|\'config/config\.php\'|\'%{etcdir}/config\.php\'|g; \
    s|\.\./config/config\.php|%{etcdir}/config\.php|g; \
    s|SM_PATH \. \'config/config_default\.php\'|\'%{etcdir}/config_default\.php\'|g; \
    s|SM_PATH \. \'config/config_local\.php\'|\'%{etcdir}/config_local\.php\'|g"

perl -pi -e "s|config/config\.php|%{etcdir}/config\.php|g; \
    s|\"config\.php\"|\"%{etcdir}/config\.php\"|g; \
    s|\"config_default\.php\"|\"%{etcdir}/config_default\.php\"|g; \
    s|\"config_local\.php\"|\"%{etcdir}/config_local\.php\"|g; \
    s|\.\./plugins|%{basedir}/plugins|g; \
    s|\.\./themes|%{basedir}/themes|g; \
    s|\>config\.php|\>%{etcdir}/config\.php|g" config/conf.pl

# hard code the path to the plugins config files

perl -pi -e "s|SM_PATH \. \'config/admins\'|\'%{pluginetc}/administrator-admins\'|g" plugins/administrator/*.php
perl -pi -e "s|SM_PATH \. \\\$SQSPELL_DIR \. \'sqspell_config\.php\'|\'%{pluginetc}/sqspell_config\.php\'|g" plugins/squirrelspell/*.php


if [ -d plugins/address_add ]; then
    echo "address_add plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE3}
	# Do not use chmod -R 644, otherwise you can't chdir to the
	# directory anymore
	chmod 644 address_add/*.php address_add/classes/*.php address_add/README
    popd
fi

if [ -d plugins/block_sender ]; then
    echo "block_sender plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE4}
	chmod 755 block_sender
	find block_sender -type f -print | xargs chmod 644
	perl -pi -e 's|data_dir \. \$username|data_dir ."/". \$username|;' block_sender/*.php
    popd
fi

if [ -d plugins/login_image ]; then
    echo "login_image plugin already present"
    sleep 360
else
    pushd plugins; tar -jxf %{SOURCE5}; chmod 0644 login_image/*.php; popd
fi
%patch5 -p0


if [ -d plugins/secure_login ]; then
    echo "secure_login plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE6}
    popd
fi
pushd plugins/secure_login
    cp -f config.php.sample config.php
popd
%patch6 -p0
perl -pi -e "s|SM_PATH \. \'plugins/secure_login/config\.php\'|\'%{pluginetc}/secure_login_config\.php\'|g" plugins/secure_login/*.php
perl -pi -e "s|\'\.\./plugins/secure_login/config\.php\'|\'%{pluginetc}/secure_login_config\.php\'|g" plugins/secure_login/*.php

if [ -d plugins/compatibility ]; then
    echo "compatibility plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE7}
	patch -p0 < compatibility/patches/compatibility_patch-1.4.6.diff
	rm -rf compatibility/patches compatibility/patches.old
	rm -f compatibility/COPYING compatibility/make_release.sh compatibility/getpot
    popd
fi

if [ -d plugins/change_pass ]; then
    echo "change_pass plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE8}
	rm -rf change_pass/courierpassd-*
	rm -f change_pass/xm locale/Makefile
%patch2 -p0
    popd
perl -pi -e "s|SM_PATH \. \'plugins/change_pass/settings.php\'|\'%{pluginetc}/change_pass_settings.php\'|g" plugins/change_pass/*.php
fi

if [ -d plugins/quota_usage ]; then
    echo "quota_usage plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE9}
	cp -f quota_usage/config.php.sample quota_usage/config.php
	rm -f quota_usage/screen.jpg quota_usage/getpot
    popd
perl -pi -e "s|SM_PATH \. \'plugins/quota_usage/config.php\'|\'%{pluginetc}/quota_usage_config.php\'|g" plugins/quota_usage/*.php
fi

if [ -d plugins/change_ldappass ]; then
    echo "change_ldappass plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE10}
    popd
    pushd plugins/change_ldappass
%patch10 -p0
	cp -f config.php.sample config.php
	perl -pi -e "s|SM_PATH \. \'config/config\.php\'|\'%{etcdir}/config\.php\'|g; \
	    s|\"\.\./plugins/change_ldappass/config\.php\"|\'%{pluginetc}/change_ldappass_config\.php\'|g" *.php
    popd
fi

if [ -d plugins/avelsieve ]; then
    echo "avelsieve plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE11}
    popd
fi
pushd plugins/avelsieve
%patch11 -p0
%patch18 -p3
    cp -f config_sample.php config.php
    rm -rf po
    perl -pi -e "s|^include \"config\.php\"\;|include \'%{pluginetc}/avelsieve_config\.php\'\;|g; \
	s|SM_PATH \. \'plugins/avelsieve/config\.php\'|\'%{pluginetc}/avelsieve_config\.php\'|g; \
	s|SM_PATH \. \'plugins/junkfolder/config\.php\'|\'%{pluginetc}/junkfolder_config\.php\'|g" *.php
popd

if [ -d plugins/windows ]; then
    echo "windows plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE12}
    popd
fi
pushd plugins/windows
    rm -f *.diff
popd

if [ -d plugins/folder_sizes ]; then
    echo "folder_sizes plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE13}
    popd
perl -pi -e "s|SM_PATH \. \"/plugins/folder_sizes/folder_sizes_config\.php\"|\'%{pluginetc}/folder_sizes_config\.php\'|g" plugins/folder_sizes/*.php
fi

if [ -d plugins/archive_mail ]; then
    echo "archive_mail plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE14}
    popd
fi

if [ -d plugins/empty_folders ]; then
    echo "empty_folders plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE15}
    popd
fi

pushd plugins/empty_folders
    cp -f config.php.sample config.php
    rm -f empty_folder.php.old getpot make_release.sh
    rm -rf patches
    perl -pi -e "s|\'config\.php\.sample\'|\'%{pluginetc}/empty_folders_config\.php\.sample\'|g; \
	s|\'config\.php\'|\'%{pluginetc}/empty_folders_config\.php\'|g" *.php
popd

if [ -d plugins/abook_import_export ]; then
    echo "abook_import_export plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE16}
    popd
perl -pi -e "s|SM_PATH \. \'plugins/abook_import_export/config_default\.php\'|\'%{pluginetc}/abook_import_export_config\.php\'|g" plugins/abook_import_export/*.php
fi

if [ -d plugins/ldifimport ]; then
    echo "ldifimport plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE17}
    popd
perl -pi -e "s|\'config.php\'|\'%{pluginetc}/ldifimport_config\.php\'|g" plugins/ldifimport/*php
fi

if [ -d plugins/username ]; then
    echo "username plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE18}
    popd
fi

pushd plugins/username
    cp -f config.php.sample config.php
    perl -pi -e "s|SM_PATH \. \'plugins/username/config\.php\'|\'%{pluginetc}/username_config\.php\'|g; \
	s|\.\./plugins/username/config\.php|%{pluginetc}/username_config\.php|g" *.php
       
popd

if [ -d plugins/bookmarks ]; then
    echo "bookmarks plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE19}
    popd
fi

pushd plugins/bookmarks
    cp -f bookmarks_data_text.php bookmarks_data.php
    chmod 644 *
popd

if [ -d plugins/select_range ]; then
    echo "select_range plugin already present"
    sleep 360
else
    pushd plugins
        tar -jxf %{SOURCE20}
    popd
fi

pushd plugins/select_range
    cp -p config.php.sample config.php
    rm -rf patch
    perl -pi -e "s|SM_PATH \. \'plugins/select_range/config\.php\'|\'%{pluginetc}/select_range_config\.php\'|g" *.php
popd

if [ -d plugins/rewrap ]; then
    echo "rewrap plugin already present"
    sleep 360
else
    pushd plugins
        tar -jxf %{SOURCE21}
    popd
fi

if [ -d plugins/spam_buttons ]; then
    echo "spam_buttons plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE22}
    popd
fi

pushd plugins/spam_buttons
    cp -p config.php.sample config.php
    rm -f getpot
    perl -pi -e "s|SM_PATH \. \'plugins/spam_buttons/config\.php\'|\'%{pluginetc}/spam_buttons_config\.php\'|g" *.php
popd

if [ -d plugins/spamassassin ]; then
    echo "spamassassin plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxvf %{SOURCE23}
	mv SquirrelSAP*/spamassassin .
	mv SquirrelSAP*/ReadMe_SquirrelSAP spamassassin/
	perl -pi -e "s|\r|\n|g" spamassassin/config.php
	perl -pi -e "s|\r|\n|g" spamassassin/options.php
	perl -pi -e "s|\r|\n|g" spamassassin/spamassassin.php
	rm -rf SquirrelSAP*
    popd
perl -pi -e "s|SM_PATH \. \'plugins/spamassassin/config\.php\'|\'%{pluginetc}/spamassassin_config\.php\'|g" plugins/spamassassin/*.php
fi

if [ -d plugins/junkfolder ]; then
    echo "junkfolder plugin already present"
    sleep 360
else
    pushd plugins
	tar -jxf %{SOURCE24}
    popd
fi

pushd plugins/junkfolder
    rm -f po/xgetpo
    perl -pi -e "s|SM_PATH \. \'plugins/junkfolder/config\.php\'|\'%{pluginetc}/junkfolder_config\.php\'|g" config.php
popd


# Don't enable SPAM RBL by default
pushd plugins/filters
%patch13 -p0
popd

# Rearrange the documentation
mv AUTHORS ChangeLog COPYING INSTALL README UPGRADE doc/
mv ReleaseNotes doc/ReleaseNotes.txt
mv themes/README.themes doc/

for f in `find plugins -name "README*" -or -name INSTALL -or -name CHANGES \
    -or -name HISTORY -or -name CHANGELOG -or -name ChangeLog -or -name FAQ`; do
    mkdir -p doc/`dirname $f`
    mv $f $_
done

# cleanup
for f in `find plugins -name COPYING -or -name LICENSE`; do
    rm -f $f
done

#mv doc/plugins/squirrelspell/doc/README doc/plugins/squirrelspell
#rmdir doc/plugins/squirrelspell/doc
mv plugins/squirrelspell/doc/* doc/plugins/squirrelspell
rm -f doc/plugins/squirrelspell/index.php
rmdir plugins/squirrelspell/doc
mv doc/index.html doc/index2.html

cat << EOF > doc/index.html
Your squirrelmail package is installed in <a href=/squirrelmail/>%{basedir}</a>, and is aliased to <a href=/webmail>/webmail</a>.
<p>
<a href=index2.html>Read documentation</a>
EOF

# Fixup various files
echo "left_refresh=300" >> data/default_pref
%patch1 -p0 -b .oldconf
for f in contrib/RPM/squirrelmail.cron contrib/RPM/config.php.redhat; do
    perl -pi -e "s|__ATTDIR__|%{attdir}|g;s|__PREFSDIR__|%{prefsdir}|g;" $f
done

cp %{SOURCE2} doc/RPM.readme

# strip away annoying ^M
find -type f | grep -v "\.gif"|grep -v "\.png"|grep -v "\.jpg"|grep -v "\.po"|grep -v "\.mo"|grep -v "\.wav"|xargs dos2unix -U

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

export DONT_RELINK=1

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{etcdir}
install -d %{buildroot}%{prefsdir}
install -d %{buildroot}%{attdir}
install -d %{buildroot}%{basedir}
install -d %{buildroot}%{crondir}
install -d %{buildroot}%{_sbindir}/

# install default_pref
install -m 0644 data/default_pref %{buildroot}%{prefsdir}

# install the config files
install -m0644 config/config*.php %{buildroot}%{etcdir}/
install -m0644 contrib/RPM/config.php.redhat %{buildroot}%{etcdir}/config.php
install -m0750 config/conf.pl %{buildroot}%{_sbindir}/squirrelmail-conf

# install index.php
install -m0644 index.php %{buildroot}%{basedir}/

# install classes
install -d -m0755 %{buildroot}%{basedir}/class
cp -pr class %{buildroot}%{basedir}

# install include
install -d -m0755 %{buildroot}%{basedir}/include
cp -pr include %{buildroot}%{basedir}

# install functions
install -d -m0755 %{buildroot}%{basedir}/functions/decode
install -d -m0755 %{buildroot}%{basedir}/functions/encode
install -m 0644 functions/*.php %{buildroot}%{basedir}/functions/
install -m 0644 functions/decode/*.php %{buildroot}%{basedir}/functions/decode
install -m 0644 functions/encode/*.php %{buildroot}%{basedir}/functions/encode

# install src
install -d -m0755 %{buildroot}%{basedir}/src
install -m 0644 src/* %{buildroot}%{basedir}/src/

# install themes
install -d -m0755 %{buildroot}%{basedir}/themes
install -m 0644 themes/*.php %{buildroot}%{basedir}/themes/
install -d -m0755 %{buildroot}%{basedir}/themes/css
install -m 0644 themes/css/*.css %{buildroot}%{basedir}/themes/css/

# install images
install -d -m0755 %{buildroot}%{basedir}/images
install -m 0644 images/* %{buildroot}%{basedir}/images/

# install the plugins
cp -rp plugins %{buildroot}%{basedir}

# install the locales.
cp -rp locale %{buildroot}%{basedir}

# install help files
cp -rp help %{buildroot}%{basedir}

# po will go into the poutils package, so just copy it
cp -rp po %{buildroot}%{basedir}

# install the cron script
install -m 0755 contrib/RPM/squirrelmail.cron %{buildroot}/%{crondir}

cat <<EOF > %{mod_conf}

Alias /webmail %{basedir}
Alias /%{name} %{basedir}

<Directory %{basedir}>

    Allow from all

    <IfModule mod_php4.c>
	php_admin_value session.bug_compat_42 0
# Otherwise can't send mails
	php_admin_value safe_mode 0
# Misc
	php_flag register_globals	off
# Other increased PHP parameters
	php_admin_value memory_limit    64M
	php_admin_value post_max_size   17M
	php_admin_value upload_max_filesize 16M
	php_admin_value max_execution_time 120
    </IfModule>

    <IfModule mod_php5.c>
	php_admin_value session.bug_compat_42 0
# Otherwise can't send mails
	php_admin_value safe_mode 0
# Misc
	php_flag register_globals	off
# Other increased PHP parameters
	php_admin_value memory_limit    64M
	php_admin_value post_max_size   17M
	php_admin_value upload_max_filesize 16M
	php_admin_value max_execution_time 120
    </IfModule>

## To force https connection
#    <IfModule mod_ssl.c>
#	SSLRequireSSL
#	SSLRequire %{SSL_CIPHER_USEKEYSIZE} >= 128
#    </IfModule>

#<LocationMatch /%{name}>
#    Options FollowSymLinks
#    RewriteEngine on
#    RewriteCond %{SERVER_PORT} !^443$
#    RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
#</LocationMatch>

</Directory>

EOF

# fix web access
%if %mdkversion < 1020
install -m0644 %{mod_conf} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{mod_conf}
%else
install -m0644 %{mod_conf} %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{mod_conf}
%endif

# Move plugin config files
mkdir -p %{buildroot}%{pluginetc}
mv %{buildroot}%{basedir}/plugins/avelsieve/config.php %{buildroot}%{pluginetc}/avelsieve_config.php
mv %{buildroot}%{basedir}/plugins/change_ldappass/config.php %{buildroot}%{pluginetc}/change_ldappass_config.php
mv %{buildroot}%{basedir}/plugins/change_pass/settings.php %{buildroot}%{pluginetc}/change_pass_settings.php
mv %{buildroot}%{basedir}/plugins/empty_folders/config.php %{buildroot}%{pluginetc}/empty_folders_config.php
#mv %{buildroot}%{basedir}/plugins/folder_sizes/folder_sizes_config.php %{buildroot}%{pluginetc}/folder_sizes_config.php
mv %{buildroot}%{basedir}/plugins/ldifimport/config.php %{buildroot}%{pluginetc}/ldifimport_config.php
mv %{buildroot}%{basedir}/plugins/quota_usage/config.php %{buildroot}%{pluginetc}/quota_usage_config.php
mv %{buildroot}%{basedir}/plugins/secure_login/config.php %{buildroot}%{pluginetc}/secure_login_config.php
mv %{buildroot}%{basedir}/plugins/squirrelspell/sqspell_config.php %{buildroot}%{pluginetc}/sqspell_config.php
mv %{buildroot}%{basedir}/plugins/username/config.php %{buildroot}%{pluginetc}/username_config.php
mv %{buildroot}%{basedir}/plugins/select_range/config.php %{buildroot}%{pluginetc}/select_range_config.php
mv %{buildroot}%{basedir}/plugins/spam_buttons/config.php %{buildroot}%{pluginetc}/spam_buttons_config.php
mv %{buildroot}%{basedir}/plugins/spamassassin/config.php %{buildroot}%{pluginetc}/spamassassin_config.php
mv %{buildroot}%{basedir}/plugins/junkfolder/config.php %{buildroot}%{pluginetc}/junkfolder_config.php
mv %{buildroot}%{basedir}/plugins/abook_import_export/config_default.php %{buildroot}%{pluginetc}/abook_import_export_config.php

# wrong locale name, would never be used, and it is duplicated with a
# correct name (just "pl")
rm -rf %{buildroot}%{basedir}/plugins/change_ldappass/locale/PL_pl

# make some po file lists
find %{buildroot} -type f -name "*.po" | sed -e 's|^%{buildroot}|%%exclude |' > exclude_pofiles.list
find %{buildroot} -type f -name "*.po" | sed -e 's|^%{buildroot}||' > pofiles.list
find %{buildroot} -type f -name "*.mo" | sed -e 's|^%{buildroot}||' > mofiles.list

ls -1d locale/*/|sed -e 's/locale\///'|sed -e 's/\///'> LOCALES

# add some extra locales here
cat >> LOCALES << EOF
th_TH
tl_PH
uk_UA
vi_VN
EOF

for i in `cat LOCALES`; do
    grep "/${i}/" mofiles.list > ${i}.list
    if [ -d help/${i} ]; then echo "%{basedir}/help/${i}" >> ${i}.list; fi
    if [ -f images/sec_remove_${i}.png ]; then echo "%{basedir}/images/sec_remove_${i}.png" >> ${i}.list; fi
    if [ -f locale/${i}/setup.php ]; then echo "%{basedir}/locale/${i}/setup.php" >> ${i}.list; fi
done

#  merge the pt and pt_BR packages as locales-pt includes locales-pt_BR but does not provide
cat pt_BR.list >> pt_PT.list

# nuke unwanted files
rm -rf contrib/RPM

# http://qa.mandriva.com/show_bug.cgi?id=27401
install -d %{buildroot}%{basedir}/conf
install -m0750 %{SOURCE25} %{buildroot}%{basedir}/conf/conf.pl

%post
# Put correct hostname in config. We do this every time, since we change the
# .rpmnew as well. This is safe even if someone already modified the config,
# because the script will not find __HOSTNAME__ in the file and will do
# nothing.
for f in %{etcdir}/config.php %{etcdir}/config.php.rpmnew \
    %{pluginetc}/avelsieve_config.php %{basedir}/plugins/avelsieve/addrule_html.php; do
    perl -pi -e "s|__HOSTNAME__|$HOSTNAME|g" $f 2>/dev/null
done

# Upgrade the configuration file using ccp if needed
# --ifexists makes sure it doesn't do anything (or whine/return nonzero)
# --ignoreopt config_version makes sure the config_version in config.php.rpmnew is kept
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{etcdir}/config.php --newfile %{etcdir}/config.php.rpmnew

# try to fix the plugins config too
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/avelsieve_config.php --newfile %{pluginetc}/avelsieve_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/change_ldappass_config.php --newfile %{pluginetc}/change_ldappass_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/change_pass_settings.php --newfile %{pluginetc}/change_pass_settings.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/empty_folders_config.php --newfile %{pluginetc}/empty_folders_config.php.rpmnew
#ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/folder_sizes_config.php --newfile %{pluginetc}/folder_sizes_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/ldifimport_config.php --newfile %{pluginetc}/ldifimport_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/quota_usage_config.php --newfile %{pluginetc}/quota_usage_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/secure_login_config.php --newfile %{pluginetc}/secure_login_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/select_range_config.php --newfile %{pluginetc}/select_range_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/spamassassin_config.php --newfile %{pluginetc}/spamassassin_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/spam_buttons_config.php --newfile %{pluginetc}/spam_buttons_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/sqspell_config.php --newfile %{pluginetc}/sqspell_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/username_config.php --newfile %{pluginetc}/username_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/junkfolder_config.php --newfile %{pluginetc}/junkfolder_config.php.rpmnew
ccp --delete --ifexists --set "NoOrphans" --ignoreopt config_version --oldfile %{pluginetc}/abook_import_export_config.php --newfile %{pluginetc}/abook_import_export_config.php.rpmnew

if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart 1>&2
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f exclude_pofiles.list
%defattr(-,root,root)
%doc doc/* contrib
%if %mdkversion < 1020
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf.d/%{mod_conf}
%else
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{mod_conf}
%endif
%dir %{etcdir}
%attr(0644,root,root) %config(noreplace) %{etcdir}/config.php
%attr(0644,root,root) %config(noreplace) %{etcdir}/config_default.php
%attr(0644,root,root) %config(noreplace) %{etcdir}/config_local.php
%dir %{pluginetc}
%attr(0644,root,root) %config(noreplace) %{pluginetc}/avelsieve_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/change_ldappass_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/change_pass_settings.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/empty_folders_config.php
#%attr(0644,root,root) %config(noreplace) %{pluginetc}/folder_sizes_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/ldifimport_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/quota_usage_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/secure_login_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/select_range_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/spamassassin_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/spam_buttons_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/sqspell_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/username_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/junkfolder_config.php
%attr(0644,root,root) %config(noreplace) %{pluginetc}/abook_import_export_config.php
%dir %{basedir}
%dir %{varlibdir}
%dir %{varspooldir}
%{basedir}/class
%{basedir}/functions
%{basedir}/help/en_US
%{basedir}/help/index.php
%{basedir}/locale/timezones.cfg
%{basedir}/locale/index.php
%{basedir}/locale/README.locales
%{basedir}/images/blank.png
%{basedir}/images/delitem.png
%{basedir}/images/down_pointer.png
%{basedir}/images/draft.png
%{basedir}/images/folder.png
%{basedir}/images/inbox.png
%{basedir}/images/index.php
%{basedir}/images/minus.png
%{basedir}/images/plus.png
%{basedir}/images/sec_remove_eng.png
%{basedir}/images/senti.png
%{basedir}/images/sm_logo.png
%{basedir}/images/sort_none.png
%{basedir}/images/up_pointer.png
%{basedir}/images/mandriva.png
%{basedir}/include
%exclude %{basedir}/plugins/address_add/locale
%exclude %{basedir}/plugins/avelsieve/locale
%exclude %{basedir}/plugins/change_ldappass/locale
%exclude %{basedir}/plugins/change_pass/locale
%exclude %{basedir}/plugins/rewrap/locale
%exclude %{basedir}/plugins/select_range/locale
%{basedir}/plugins/index.php
# bundled plugins
%{basedir}/plugins/abook_take
%{basedir}/plugins/administrator
%{basedir}/plugins/bug_report
%{basedir}/plugins/calendar
%{basedir}/plugins/delete_move_next
%{basedir}/plugins/filters
%{basedir}/plugins/fortune
%{basedir}/plugins/info
%{basedir}/plugins/listcommands
%{basedir}/plugins/mail_fetch
%{basedir}/plugins/message_details
%{basedir}/plugins/newmail
%{basedir}/plugins/sent_subfolders
%{basedir}/plugins/spamcop
%{basedir}/plugins/squirrelspell
%{basedir}/plugins/translate
# added plugins
%{basedir}/plugins/abook_import_export
%{basedir}/plugins/address_add
%{basedir}/plugins/archive_mail
%{basedir}/plugins/avelsieve
%{basedir}/plugins/block_sender
%{basedir}/plugins/bookmarks
%{basedir}/plugins/change_ldappass
%{basedir}/plugins/change_pass
%{basedir}/plugins/compatibility
%{basedir}/plugins/empty_folders
%{basedir}/plugins/folder_sizes
%{basedir}/plugins/ldifimport
%{basedir}/plugins/login_image
%{basedir}/plugins/quota_usage
%{basedir}/plugins/rewrap
%{basedir}/plugins/secure_login
%{basedir}/plugins/select_range
%{basedir}/plugins/spamassassin
%{basedir}/plugins/spam_buttons
%{basedir}/plugins/username
%{basedir}/plugins/windows
%{basedir}/plugins/junkfolder
%{basedir}/src
%{basedir}/themes
%{basedir}/index.php
%attr(0750,root,root) %{_sbindir}/squirrelmail-conf
%attr(0750,root,root) %{basedir}/conf/conf.pl
%attr(0770,root,apache) %dir %{prefsdir}
%attr(0730,root,apache) %dir %{attdir}
%{prefsdir}/default_pref
%{crondir}/squirrelmail.cron

%files poutils -f pofiles.list
%defattr(-,root,root)
%{basedir}/po

%files cyrus
%defattr(-,root,root)

%files ar -f ar.list
%defattr(-,root,root)

%files bg -f bg_BG.list
%defattr(-,root,root)

%files bn -f bn_IN.list
%defattr(-,root,root)

%files ca -f ca_ES.list
%defattr(-,root,root)

%files cs -f cs_CZ.list
%defattr(-,root,root)

%files cy -f cy_GB.list
%defattr(-,root,root)

%files da -f da_DK.list
%defattr(-,root,root)

%files de -f de_DE.list
%defattr(-,root,root)

%files el -f el_GR.list
%defattr(-,root,root)

%files en -f en_GB.list
%defattr(-,root,root)

%files es -f es_ES.list
%defattr(-,root,root)

%files et -f et_EE.list
%defattr(-,root,root)

%files eu -f eu_ES.list
%defattr(-,root,root)

%files fa -f fa_IR.list
%defattr(-,root,root)

%files fi -f fi_FI.list
%defattr(-,root,root)

%files fo -f fo_FO.list
%defattr(-,root,root)

%files fr -f fr_FR.list
%defattr(-,root,root)

%files he -f he_IL.list
%defattr(-,root,root)

%files hr -f hr_HR.list
%defattr(-,root,root)

%files hu -f hu_HU.list
%defattr(-,root,root)

%files id -f id_ID.list
%defattr(-,root,root)

%files is -f is_IS.list
%defattr(-,root,root)

%files it -f it_IT.list
%defattr(-,root,root)

%files ja -f ja_JP.list
%defattr(-,root,root)

%files ko -f ko_KR.list
%defattr(-,root,root)

%files lt -f lt_LT.list
%defattr(-,root,root)

%files ms -f ms_MY.list
%defattr(-,root,root)

# "no" is a deprecated language code for "nb"
%files nb -f nb_NO.list
%defattr(-,root,root)

%files nl -f nl_NL.list
%defattr(-,root,root)

%files nn -f nn_NO.list
%defattr(-,root,root)

%files pl -f pl_PL.list
%defattr(-,root,root)

%files pt -f pt_PT.list
%defattr(-,root,root)

#%files pt_BR -f pt_BR.list
#%defattr(-,root,root)

%files ro -f ro_RO.list
%defattr(-,root,root)

%files ru -f ru_RU.list
%defattr(-,root,root)

%files sk -f sk_SK.list
%defattr(-,root,root)

%files sl -f sl_SI.list
%defattr(-,root,root)

%files sr -f sr_YU.list
%defattr(-,root,root)

%files sv -f sv_SE.list
%defattr(-,root,root)

%files th -f th_TH.list
%defattr(-,root,root)

%files tl -f tl_PH.list
%defattr(-,root,root)

%files tr -f tr_TR.list
%defattr(-,root,root)

%files ug -f ug.list
%defattr(-,root,root)

%files uk -f uk_UA.list
%defattr(-,root,root)

%files vi -f vi_VN.list
%defattr(-,root,root)

%files zh_CN -f zh_CN.list
%defattr(-,root,root)

%files zh_TW -f zh_TW.list
%defattr(-,root,root)

%files ka -f ka.list
%defattr(-,root,root)
