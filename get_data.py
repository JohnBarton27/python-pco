import pprint
import pypco
from lib.planning_center import PlanningCenter as PCO
from datetime import datetime, timedelta

# Setup Pretty Printer
pp = pprint.PrettyPrinter(indent=4)

# Get an instance of the PCO object using your personal access token.
pco = PCO("705ffca009ccf550dca04197586e4f4e2faf1398e9e5df1f5e29afccdaaa7292", "7ff8e268c6b2331503937e8bfed3887b03c21fd3e943e2a3bd2f5c26f7fd3d10")


output = pco.get('/services/v2/service_types')
pp.pprint(output)
# names = [service_type["attributes"]["name"] for service_type in output["data"]]
# ids = [service_type["id"] for service_type in output["data"]]
#
# pp.pprint(output)
# pp.pprint(names)
# pp.pprint(ids)

# gathering_type_id = "68383"
#
# # Get the next Sunday
# this_sunday = datetime.now()
# this_sunday = this_sunday.replace(hour=23, minute=59)
# while this_sunday.weekday() != 6:
#     this_sunday += timedelta(days=1)
#
# # Get the service for this Sunday
# service_order = pco.iterate("/services/v2/service_types/{}/plans?order=-sort_date".format(gathering_type_id))
# while True:
#     service = next(service_order)
#     service_date = datetime.strptime(service["data"]["attributes"]["sort_date"], "%Y-%m-%dT%H:%M:%SZ")
#
#     if service_date < this_sunday:
#         break
#
# service_id = service["data"]["id"]
# service_order = pco.get("/services/v2/service_types/{}/plans/{}/items".format(gathering_type_id, service_id))
#
# description = "Thanks for joining us for our Online Contemporary Service!\n\nHere is a snapshot of today's service:\n"
# for item in service_order["data"][1:]:
#     description += "\n\t" + item["attributes"]["title"]
#
# print(description)

