use std::ops::Index;
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

fn check(v: Vec<Vec<char>>, n:i32, m:i32 ){

    let vika = "vika".to_string();
    let mut index = 0;

    for (i,_) in v.iter().enumerate() {
        if index==4{
            println!("YES");
            break;
        }
        for j in v.iter().enumerate(){

            let iv = v.index(i);
            if vika.chars().nth(index).unwrap() == *iv.index(j){
                index +=1;
                break;
            }

        }
    }
    if index < 4 {
        println!("NO");
    }

}

fn main(){

    read!(t as i32);
    for _ in 0..t{
        read_vec!(nm as i32);
        let (n,m) = (nm[0],nm[1]);

        let mut v: Vec<Vec<char>> = vec![] ;
        for _ in 0..n {
            read_vec!(nm as char);
            v.push(nm);
        }



    }

}