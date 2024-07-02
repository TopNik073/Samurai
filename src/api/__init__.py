from src.api.businesses import router as router_businesses
from src.api.users import router as router_users
from src.api.admins import router as router_admins


api_routers = [router_businesses, router_users, router_admins]
