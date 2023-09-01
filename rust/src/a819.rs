#[allow(unused_macros)]
macro_rules! read {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let $out = inner.trim().parse::<$type>().expect("Parsable");
    };
}

#[allow(unused_macros)]
macro_rules! read_str {
    ($out:ident) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let $out = inner.trim();
    };
}

#[allow(unused_macros)]
macro_rules! read_vec {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).unwrap();
        let $out = inner
            .trim()
            .split_whitespace()
            .map(|s| s.parse::<$type>().unwrap())
            .collect::<Vec<$type>>();
    };
}

fn main() {
    read!(tests as u32);

    for _ in 1..=tests {
        read_str!(my_str);
        let _ = my_str.trim();
        let size = my_str.len();

        if my_str == "()"{
            println!("NO");
            continue;
        }
        println!("YES");

        let s= "()".repeat(size);
        if s.contains(my_str){
            println!("{}", s);
            continue;
        };

        let s2= "(".repeat(size) + &")".repeat(size);
        println!("{}",s2);

    }
}
