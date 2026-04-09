import java.io.BufferedReader;

import java.io.IOException;

import java.io.InputStreamReader;

import java.util.StringTokenizer;



public class Main {

public static void main(String[] args) throws IOException {

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

StringTokenizer st = new StringTokenizer(br.readLine());

int K = Integer.parseInt(st.nextToken());

int N = Integer.parseInt(st.nextToken());

int[] lens = new int[N];



for(int i = 0; i < K; i++) lens[i] = Integer.parseInt(br.readLine());

long high = (long) Math.pow(2,32);

long low = 0;

long max_size = 0;

while (low <= high){

long mid = (high+low)/2;

long num = 0;

for(int i = 0; i < N; i++){

num += lens[i]/mid;

}

if(num < N) {

high = mid-1;

}else {

max_size = Math.max(max_size, mid);

low = mid+1;

}

// System.out.println("high: "+ high);

// System.out.println("low: "+ low);

// System.out.println("mid: "+ mid);

// System.out.println("`````````````````");



}

System.out.println(max_size);

}

}