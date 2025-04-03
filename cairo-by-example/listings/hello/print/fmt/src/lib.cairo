use core::fmt::{Formatter, Display};
use core::fmt;

#[derive(Drop)]
struct City {
    name: ByteArray,
    // Latitude
    lat: i32,
    // Longitude
    lon: i32,
}

impl CityDisplay of Display<City> {
    // `f` is a buffer, and this method must write the formatted string into it.
    fn fmt(self: @City, ref f: Formatter) -> Result<(), fmt::Error> {
        let lat_c = if *self.lat >= 0 {
            'N'
        } else {
            'S'
        };
        let lon_c = if *self.lon >= 0 {
            'E'
        } else {
            'W'
        };

        // `write!` is like `format!`, but it will write the formatted string
        // into a buffer (the first argument).
        write!(f, "{}: {}'{} {}'{}", self.name, *self.lat, lat_c, *self.lon, lon_c)
    }
}

#[derive(Debug, Copy, Drop)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    let dublin = City { name: "Dublin", lat: 53, lon: -6 };
    let oslo = City { name: "Oslo", lat: 59, lon: 10 };
    let vancouver = City { name: "Vancouver", lat: 49, lon: -123 };

    println!("{}", dublin);
    println!("{}", oslo);
    println!("{}", vancouver);

    let colors = array![
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ];

    let mut i = 0;
    loop {
        if i >= colors.len() {
            break;
        }
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{:?}", *colors.at(i));
        i += 1;
    }
}
