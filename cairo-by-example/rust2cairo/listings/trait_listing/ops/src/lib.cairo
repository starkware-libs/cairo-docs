struct Potion {
    health: u64,
    mana: u64,
}

// The `Add` trait is used to specify the functionality of `+`.
// Here, we make `Add<Potion>` - the trait for addition with a LHS and RHS of type `Potion`.
// The following block implements the operation: Potion + Potion = Potion
impl PotionAdd of Add<Potion> {
    fn add(lhs: Potion, rhs: Potion) -> Potion {
        Potion { health: lhs.health + rhs.health, mana: lhs.mana + rhs.mana }
    }
}

fn main() {
    let health_potion: Potion = Potion { health: 100, mana: 0 };
    let mana_potion: Potion = Potion { health: 0, mana: 100 };
    let super_potion: Potion = health_potion + mana_potion;
    // Both potions were combined with the `+` operator.
    assert(super_potion.health == 100, '');
    assert(super_potion.mana == 100, '');
}
