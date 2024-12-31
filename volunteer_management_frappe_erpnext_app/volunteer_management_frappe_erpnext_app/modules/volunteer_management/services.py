# volunteer_management_frappe_erpnext_app/volunteer_management_frappe_erpnext_app/modules/volunteer_management/services.py

import frappe
import redis
import os

class RedisCache:
    """
    Singleton class for Redis cache.
    Ensures only one connection is open at a time for the entire app.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisCache, cls).__new__(cls)
            cls._instance.connection = redis.Redis(
                host=os.getenv('REDIS_HOST', 'localhost'),
                port=os.getenv('REDIS_PORT', 6379),
                db=0
            )
        return cls._instance

def cache_volunteer_data(volunteer_email: str, data: dict):
    """
    Cache volunteer data to Redis for quick lookups (improving performance).
    """
    cache = RedisCache().connection
    cache.set(f"volunteer:{volunteer_email}", frappe.as_json(data))

def get_cached_volunteer_data(volunteer_email: str):
    cache = RedisCache().connection
    cached_data = cache.get(f"volunteer:{volunteer_email}")
    if cached_data:
        return frappe.parse_json(cached_data)
    return None
