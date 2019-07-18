# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging
import random

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

TURNON_INTENT = "JIYAN_TurnOn"

SKILL_NAME = "Trinkspruch"

ANSWERS = ["AAAbkacken! AAAbkacken! AAAbkacken!",
           "Aufgehts! Aufgehts! Aufgehts!",
           "Genug getrunken, jetzt wird gesoffen!",
           "Stößchen! Wie man unter Männern sagt.",
           "Von der Wiege bis zur Bahre ist der Suff das einzig Wahre!",
           "Es trinkt der Mensch es säuft das Pferd: nur heute ist es "
           "umgekehrt.",
           "Sport ist Mord, nur Sprit hält fit",
           "Zwischen Leber und Nierchen passt immer ein Bierchen.",
           "Das Leben ist an manchen Tagen, halt nur im Vollrausch zu "
           "ertragen.",
           "Morgens ein Bier und der Tag gehört Dir!",
           "Bier ist lecker, Bier ist toll, am liebsten bin ich voll!",
           "Der kluge Mensch, glaubt es mir, der redet nicht und trinkt sein "
           "Bier.",
           "Auch Wasser wird zum edlen Tropfen, mischt man es mit Malz und "
           "Hopfen.",
           "Wein auf Bier, das rat’ ich dir! Bier auf Wein, dass lass’ sein!",
           "Flüssig Brot macht Wangen rot!",
           "Wenn ich Deinen Hals berühre, Deinen Mund an meinen führe, ach, "
           "wie sehn´ ich mich nach Dir, heissgeliebte Flasche Bier!",
           "Lass dich nicht lumpen, hoch den Humpen!",
           "Ein Gläschen in Ehren kann niemand verwehren.",
           "Lieber in der dunkelsten Kneipe als am hellsten Arbeitsplatz.",
           "Zwei Fliegen tanzten  wippe wippe, auf der Jungferaus "
           "Schameslippe, doch die Gute musste brunzen und das ganze Spiel"
           "verhunzen. Prost!",
           "Was früher meine Leber war, ist heute eine Minibar!",
           "Nich' lang schnacken, Kopp innen Nacken!",
           "Bist du voll so leg dich nieder, nach dem Schlafen saufe wieder.",
           "Korn, Bier, Schnaps und Wein und wir hören unsere Leber schrein!",
           "Lasst euch nicht lumpen, hoch mit dem Humpen!",
           "Ein Gläschen in Ehren kann niemand verwehren.",
           "Gott erfand den Wein, Gott erfand das Bier, doch den Schnaps den "
           "brannten wir.",
           "Zwischen Leber und Milz passt immer noch ein Pils."

           ]


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for no specified Intent."""

    def can_handle(self, handler_input):
        request_type = is_request_type("LaunchRequest")(handler_input)

        if request_type:
            return True

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        handler_input.response_builder.speak(
            random.choice(ANSWERS))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Sag einfach \"Alexa Trinkspruch!\""

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard("Hello World", speech_text))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Schöne Besäufnis noch!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text))
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = (
            "Lass uns richtig blöd saufen!")
        reprompt = "You can say hello!!"
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Ich habe dich leider nicht verstanden Bruder"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
