set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Checking if superuser should be created..."
if [ "$CREATE_SUPERUSER" = "1" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --no-input || echo "Superuser creation failed."
fi
