#!/usr/bin/env python
"""
Helper script to create an admin user for Techternet blog.
Run this script to create a superuser for the Django admin panel.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techternet.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    username = input("Enter admin username (default: admin): ").strip() or "admin"
    email = input("Enter admin email (default: admin@techternet.com): ").strip() or "admin@techternet.com"
    password = input("Enter admin password (default: admin123): ").strip() or "admin123"
    
    if User.objects.filter(username=username).exists():
        print(f"\nUser '{username}' already exists!")
        return
    
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    
    print(f"\n✓ Superuser '{username}' created successfully!")
    print(f"  Email: {email}")
    print(f"\nYou can now login to the admin panel at: /admin/")
    print(f"  Username: {username}")
    print(f"  Password: {password}")

if __name__ == "__main__":
    print("=" * 50)
    print("Techternet Admin User Creation")
    print("=" * 50)
    create_admin()
