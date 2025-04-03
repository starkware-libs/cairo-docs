#[derive(Drop)]
struct NonCopyU8 {
    inner: u8,
}

// This function takes ownership of type that is not copyable
fn eat_noncopy_u8(noncopy_u8: NonCopyU8) {
    println!("Dropping a non copyable type that contains {}", noncopy_u8.inner);
}

// This function takes a snapshot of a non-copyable type
fn snapshot_noncopy(snapshot_noncopy_u8: @NonCopyU8) {
    println!("This non-copyable type contains {}", snapshot_noncopy_u8.inner);
}

// This function takes a snapshot of a copyable type
fn snapshot_copyable(snapshot_copyable_u8: @u8) {
    println!("This copyable type contains {}", snapshot_copyable_u8);
}

fn main() {
    // Create a both a copyable and non-copyable type.
    let copyable_u8 = 5_u8;
    let noncopy_u8 = NonCopyU8 { inner: 5_u8 };

    // Take snapshots of the contents. Ownership is not taken,
    // so the contents can be snapshotted again.
    snapshot_noncopy(@noncopy_u8);
    snapshot_copyable(@copyable_u8);

    {
        // Take a snapshot of the data contained inside the box
        let snap_to_noncopy: @NonCopyU8 = @noncopy_u8;

        // This is allowed! Snapshots are immutable views
        // so we can still use noncopy_u8 even while snapshots exist
        eat_noncopy_u8(noncopy_u8);

        // We can still use the snapshot after the original variable is dropped
        // since snapshots are just views of immutable memory cells
        snapshot_noncopy(snap_to_noncopy);
        // `snap_to_noncopy` goes out of scope
    }
    // We can't use noncopy_u8 here since ownership was transferred to eat_noncopy_u8
// eat_noncopy_u8(noncopy_u8); // This would fail to compile
}
