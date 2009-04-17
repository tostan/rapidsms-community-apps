#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

#Views for handling summary of Reports Displayed as Location Tree
def supply_summary(req), locid:
    return render_to_response("nigeria/supply_summary.html", context_instance=RequestContext(req))

def bednets_summary(req, locid):
    return render_to_response("nigeria/bednets_summary.html", context_instance=RequestContext(req))

def coupons_summary(req, locid):
    return render_to_response("nigeria/coupons_summary.html", context_instance=RequestContext(req))


# Periodical Reporting  by day, week, month for coupons
def coupons_daily(req, locid=0):
    return render_to_response("nigeria/coupons_daily.html", context_instance=RequestContext(req))

def coupons_weekly(req, locid):
    return render_to_response("nigeria/coupons_weekly.html", context_instance=RequestContext(req))

def coupons_monthly(req, locid):
    return render_to_response("nigeria/coupons_monthly.html", context_instance=RequestContext(req))


# Periodical Reporting  by day, week, month for bednets
def bednets_daily(req, locid):
    return render_to_response("nigeria/bednets_daily.html", context_instance=RequestContext(req))

def bednets_weekly(req, locid):
    return render_to_response("nigeria/bednets_weekly.html", context_instance=RequestContext(req))

def bednets_monthly(req, locid):
    return render_to_response("nigeria/bednets_monthly.html", context_instance=RequestContext(req))


# Periodical Reporting  by day, week, month for supply
def supply_daily(req, locid):
    return render_to_response("nigeria/supply_daily.html", context_instance=RequestContext(req))

def supply_weekly(req, locid):
    return render_to_response("nigeria/supply_weekly.html", context_instance=RequestContext(req))

def supply_monthly(req, locid):
    return render_to_response("nigeria/supply_monthly.html", context_instance=RequestContext(req))

#This is a testing view
def test(req):
    return render_to_response("nigeria/testpages/tests.html", context_instance=RequestContext(req))

