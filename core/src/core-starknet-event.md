# event

Event handling traits for Starknet smart contracts.
This module provides traits for serializing, deserializing and emitting events on Starknet.
The [`Event`](./core-starknet-event-Event.md) trait handles the serialization of event types, while the `EventEmitter` trait
provides the capability to emit events from Starknet contracts.

Fully qualified path: [core](./core.md)::[starknet](./core-starknet.md)::[event](./core-starknet-event.md)


[Traits](./core-starknet-event-traits.md)
 ---
| | |
|:---|:---|
| [Event](./core-starknet-event-Event.md) | A trait for handling serialization and deserialization of events. Events in Starknet are stored in transaction receipts as a combination of keys and data fields.[...](./core-starknet-event-Event.md) |
| [EventEmitter](./core-starknet-event-EventEmitter.md) | A trait for emitting Starknet events.[...](./core-starknet-event-EventEmitter.md) |
