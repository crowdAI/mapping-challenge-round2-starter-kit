#!/usr/bin/env python
import crowdai_api
import os

########################################################################
# Instatiate Event Notifier
########################################################################
crowdai_events = crowdai_api.events.CrowdAIEvents()


def execution_start():
    ########################################################################
    # Register Evaluation Start event
    ########################################################################
    crowdai_events.register_event(
                event_type=crowdai_events.CROWDAI_EVENT_INFO,
                message="execution_started",
                payload={ #Arbitrary Payload
                    "event_type": "mapping_challenge:execution_started"
                    }
                )


def execution_progress(progress_payload):
    image_ids = progress_payload["image_ids"]
    ########################################################################
    # Register Evaluation Progress event
    ########################################################################
    crowdai_events.register_event(
                event_type=crowdai_events.CROWDAI_EVENT_INFO,
                message="execution_progress",
                payload={ #Arbitrary Payload
                    "event_type": "mapping_challenge:execution_progress",
                    "image_ids" : image_ids
                    }
                )

def execution_success(payload):
    predictions_output_path = payload["predictions_output_path"]
    ########################################################################
    # Register Evaluation Complete event
    ########################################################################
    expected_output_path = os.getenv("CROWDAI_PREDICTIONS_OUTPUT_PATH", False)
    if expected_output_path != predictions_output_path:
        raise Exception("Please write the output to the path specified in the environment variable : CROWDAI_PREDICTIONS_OUTPUT_PATH instead of {}".format(predictions_output_path))

    crowdai_events.register_event(
                event_type=crowdai_events.CROWDAI_EVENT_SUCCESS,
                message="execution_success",
                payload={ #Arbitrary Payload
                    "event_type": "mapping_challenge:execution_success",
                    "predictions_output_path" : predictions_output_path
                    },
                blocking=True
                )

def execution_error(error):
    ########################################################################
    # Register Evaluation Complete event
    ########################################################################
    crowdai_events.register_event(
                event_type=crowdai_events.CROWDAI_EVENT_ERROR,
                message="execution_error",
                payload={ #Arbitrary Payload
                    "event_type": "mapping_challenge:execution_error",
                    "error" : error
                    },
                blocking=True
                )
