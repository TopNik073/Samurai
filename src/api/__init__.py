from api.businesses import router as router_businesses
from api.users import router as router_users
from api.admins import router as router_admins
from OAuth.Manager import router as router_oauth

api_routers = [router_businesses, router_users, router_admins]
