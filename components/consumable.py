from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import util.actions as actions
import util.color as color
import components.inventory
from components.base_component import BaseComponent
from util.exceptions import Impossible

if TYPE_CHECKING:
    from entity.entity import Actor, Item

class Consumable(BaseComponent):
    parent: Item

    def get_action(self, consumer: Actor) -> Optional[actions.Action]:
        """
            Try to return the aciton for this item
        """
        return actions.ItemAction(consumer, self.parent)
    
    def activate(self, action: actions.ItemAction) -> None:
        """
            Invoke this item's ability.

            `action` is the context for this activation.
        """
        raise NotImplementedError()
    
    def consume(self) -> None:
        """
            Remove the consumed item from parent's inventory
        """
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)
    
class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount
    
    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)

        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                color.health_recoverd,
            )
            self.consume()
        else:
            raise Impossible("Your health is already full.")