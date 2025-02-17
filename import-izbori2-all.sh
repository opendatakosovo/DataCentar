#!/bin/sh
source ./venv/bin/activate

#parlamentarni
python import-izbori.py --election parlamentarni --year 2003 --granular
python import-izbori.py --election parlamentarni --year 2007 --granular
python import-izbori.py --election parlamentarni --year 2008 --granular
python import-izbori.py --election parlamentarni --year 2012 --granular
python import-izbori.py --election parlamentarni --year 2014 --granular
python import-izbori.py --election parlamentarni --year 2016 --granular

python import-izbori.py --election predsjednicki --year 2002 --month decembar --round prvi --status nema --granular
python import-izbori.py --election predsjednicki --year 2002 --month decembar --round drugi --status nema --granular
python import-izbori.py --election predsjednicki --year 2002 --month decembar --round prvi --status ponovljeni --granular
python import-izbori.py --election predsjednicki --year 2003 --month november --round prvi --status nema --granular

python import-izbori.py --election predsjednicki --year 2004 --month juna --round prvi --status nema --granular
python import-izbori.py --election predsjednicki --year 2004 --month juna --round drugi --status nema --granular

python import-izbori.py --election predsjednicki --year 2008 --month januar --round prvi --status nema --granular
python import-izbori.py --election predsjednicki --year 2008 --month februari --round drugi --status nema --granular

python import-izbori.py --election predsjednicki --year 2012 --month maja --round prvi --status nema --granular
python import-izbori.py --election predsjednicki --year 2012 --month maja --round drugi --status nema --granular

python import-izbori.py --election predsjednicki --year 2017 --month april --round prvi --status nema --granular