from . import coffee
from flask import request, jsonify, make_response
from app.models import CoffeeMachine, CoffeePod


@coffee.route('/machine/create', methods=['GET', 'POST'])
def create_machine():
    """Endpoint for creating new coffee machine mongo document"""
    if request.method == 'GET':
        return make_response(jsonify(
            {'message': 'you can create coffee machines '})), 200


@coffee.route('/machine/filter', methods=['GET', 'POST'])
def filter_machine():
    """Endpoint for querying coffee machine mongo documents by filter/s"""
    if request.method == 'GET':
        return make_response(jsonify(
            {'message':
             'you can filter coffee machines by their attributes'})), 200
    if request.method == 'POST':
        # get request json body to use as a raw filter for mongoengine
        raw_filter = request.get_json()
        # use body to filter machine objects
        machines = CoffeeMachine.objects(__raw__=raw_filter)
        # make a list of machines codes
        machines_codes = [machine.code for machine in machines]
        # return a filtered list of machines
        return make_response(jsonify(machines_codes))


@coffee.route('/pod/create', methods=['GET', 'POST'])
def create_pod():
    """Endpoint for creating new coffee pod mongo document"""
    if request.method == 'GET':
        return make_response(jsonify(
            {'message': 'you can create coffee pods '})), 200


@coffee.route('/pod/filter', methods=['GET', 'POST'])
def filter_pod():
    """Endpoint for querying coffee pod mongo documents by filter/s"""
    if request.method == 'GET':
        return make_response(jsonify(
            {'message':
             'you can filter coffee pods by their attributes'})), 200

    if request.method == 'POST':
        # get request json body to use as a raw filter for mongoengine
        raw_filter = request.get_json()
        # use body to filter pod objects
        pods = CoffeePod.objects(__raw__=raw_filter)
        # make a list of pods codes
        pods_codes = [pod.code for pod in pods]
        # return a filtered list of pods
        return make_response(jsonify(pods_codes))
