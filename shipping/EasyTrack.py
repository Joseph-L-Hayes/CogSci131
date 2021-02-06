import easypost
import json
import pprint
import dateutil.parser

easypost.api_key = "EZAKb193184e1f024f9c95f111715747fde0WzgPIAuaif3aYAwDBwYkaA"

track_numbers = [("fedex","954415965971"), ("ups","1Z9437070322066511"), ("dhl express","4581466982"), ("ups","1ZR0967V0317476280"), ("usps", "9361289676091220806715"), ("ups","1ZEA54790393379970")]

def track(track_id):

    tracker = easypost.Tracker.create(
        tracking_code=track_id[1],
        carrier=track_id[0]
    )

    print("Estimated Delivery Date:", dateConvert(tracker["est_delivery_date"]))

    for s in tracker["tracking_details"]:

        tracking = s["tracking_location"]["city"]
        date = dateConvert(s["datetime"])

        print(str(date) + ':', str(tracking) + "," , s["message"])

def dateConvert(isoDate):
    """Converts an iso 8601 date to more readable format."""

    if isoDate != None:
        return dateutil.parser.parse(isoDate)
    else:
        return 'Not Available'



for t in track_numbers:
    track(t)
    print()


#Output from Fedex shipping number:
# FedEx
# 167965771614
# delivered
# [<EasyPostObject b'TrackingDetail' at 0x10de65ed0> JSON: {
#   "carrier_code": "OC",
#   "datetime": "2020-06-30T12:37:35Z",
#   "description": "Shipment information sent to FedEx",
#   "message": "Shipment information sent to FedEx",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "pre_transit",
#   "status_detail": "label_created",
#   "tracking_location": {
#     "city": null,
#     "country": null,
#     "object": "TrackingLocation",
#     "state": null,
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de65dd0> JSON: {
#   "carrier_code": "PU",
#   "datetime": "2020-06-30T19:55:00Z",
#   "description": "Picked up",
#   "message": "Picked up",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "received_at_origin_facility",
#   "tracking_location": {
#     "city": "ATLANTA",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "GA",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de65e50> JSON: {
#   "carrier_code": "AR",
#   "datetime": "2020-07-01T04:31:00Z",
#   "description": "Arrived at FedEx location",
#   "message": "Arrived at FedEx location",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "received_at_origin_facility",
#   "tracking_location": {
#     "city": "INDIANAPOLIS",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "IN",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de65fd0> JSON: {
#   "carrier_code": "DP",
#   "datetime": "2020-07-01T21:11:00Z",
#   "description": "Departed FedEx location",
#   "message": "Departed FedEx location",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "departed_facility",
#   "tracking_location": {
#     "city": "INDIANAPOLIS",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "IN",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de65f10> JSON: {
#   "carrier_code": "AR",
#   "datetime": "2020-07-02T01:19:00Z",
#   "description": "Arrived at FedEx location",
#   "message": "Arrived at FedEx location",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "received_at_origin_facility",
#   "tracking_location": {
#     "city": "OAKLAND",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "CA",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de28850> JSON: {
#   "carrier_code": "DP",
#   "datetime": "2020-07-02T11:46:00Z",
#   "description": "Departed FedEx location",
#   "message": "Departed FedEx location",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "departed_facility",
#   "tracking_location": {
#     "city": "OAKLAND",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "CA",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de28750> JSON: {
#   "carrier_code": "AR",
#   "datetime": "2020-07-02T14:07:00Z",
#   "description": "At local FedEx facility",
#   "message": "At local FedEx facility",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "in_transit",
#   "status_detail": "received_at_destination_facility",
#   "tracking_location": {
#     "city": "SAN FRANCISCO",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "CA",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de28810> JSON: {
#   "carrier_code": "OD",
#   "datetime": "2020-07-02T15:11:00Z",
#   "description": "On FedEx vehicle for delivery",
#   "message": "On FedEx vehicle for delivery",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "out_for_delivery",
#   "status_detail": "out_for_delivery",
#   "tracking_location": {
#     "city": "SAN FRANCISCO",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "CA",
#     "zip": null
#   }
# }, <EasyPostObject b'TrackingDetail' at 0x10de285d0> JSON: {
#   "carrier_code": "DL",
#   "datetime": "2020-07-02T23:08:00Z",
#   "description": "Delivered",
#   "message": "Delivered (Left at front door. Package delivered to recipient address - release authorized)",
#   "object": "TrackingDetail",
#   "source": "FedEx",
#   "status": "delivered",
#   "status_detail": "arrived_at_destination",
#   "tracking_location": {
#     "city": "San Francisco",
#     "country": null,
#     "object": "TrackingLocation",
#     "state": "CA",
#     "zip": null
#   }
# }]

#REI UPS Output:
# 2020-06-26T23:59:59Z: Tacoma, Origin Scan
# 2020-06-27T07:39:00Z: Portland, Arrived at Facility
# 2020-06-27T08:50:00Z: Portland, Departed from Facility
# 2020-06-27T12:35:00Z: Roseburg, Arrived at Facility
# 2020-06-29T10:56:00Z: Roseburg, Departed from Facility
# 2020-06-29T12:05:00Z: Grants Pass, Arrived at Facility
# 2020-06-29T14:11:00Z: Grants Pass, Departed from Facility
# 2020-06-29T18:28:00Z: Anderson, Arrived at Facility
# 2020-06-29T19:05:00Z: Anderson, Departed from Facility
# 2020-06-29T23:23:00Z: Oakland, Arrived at Facility
# 2020-06-30T04:36:00Z: Oakland, Departed from Facility
# 2020-06-30T05:12:00Z: San Francisco, Arrived at Facility
# 2020-06-30T06:41:47Z: San Francisco, Destination Scan
# 2020-06-30T07:43:43Z: San Francisco, Loaded on Delivery Vehicle
# 2020-06-30T08:40:55Z: San Francisco, Out For Delivery Today
# 2020-06-30T14:16:02Z: SAN FRANCISCO, Delivered: Reception

#Old code:
#Fedex OB shirt
# tracker = easypost.Tracker.create(
#     tracking_code="167965771614",
#     carrier="fedex"
# ) #works!
#
# #UPS REI watch
# tracker2 = easypost.Tracker.create(
#     tracking_code="1Z9437070322066511",
#     carrier="ups"
# ) #works!
#
# tracker3 = easypost.Tracker.create(
#     tracking_code="4581466982",
#     carrier="dhl express"
# ) #works!
#
# tracker4 = easypost.Tracker.create(
#     tracking_code="1ZR0967V0317476280"
# )#works without carrier

#est_delivery date is showing as None for all carriers, what is the issue?

# for s in tracker4["tracking_details"]:
#     tracking = s["tracking_location"]["city"]
#     date = s["datetime"]
#     if tracking != None:
#         print(date + ':', tracking + "," , s["message"])
