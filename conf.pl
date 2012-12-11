#!/usr/bin/perl

print "This is a simple wrapper script that calls /usr/sbin/squirrelmail-conf\n";
print "In Mandriva this \"conf.pl\" file is renamed and moved to \"/usr/sbin/squirrelmail-conf\"\n\n";
sleep "2";
exec ('/usr/sbin/squirrelmail-conf') or print STDERR "couldn't exec /usr/sbin/squirrelmail-conf: $!";
