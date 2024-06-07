
try {
    python manage.py makemigrations
    python manage.py migrate
    # python manage.py createsuperuser
    python manage.py runserver
}
catch {
    Write-Error $_.Exception.Message
    pause
}

pause
