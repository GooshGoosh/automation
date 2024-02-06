#!/bin/bash

/home/student-03-8093d4a4c4ba/ticky_check.py /home/student-03-8093d4a4c4ba/syslog.log
if [[ -e /home/student-03-8093d4a4c4ba/error_message.csv ]]; then
    /home/student-03-8093d4a4c4ba/csv_to_html.py error_message.csv /var/www/html/error_message.html
fi

if [[ -e /home/student-03-8093d4a4c4ba/user_statistics.csv ]]; then
    /home/student-03-8093d4a4c4ba/csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
fi
