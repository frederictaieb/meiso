//
//  ContentView.swift
//  JSON
//
//  Created by Frédéric TAIEB on 19/10/2019.
//  Copyright © 2019 Frédéric TAIEB. All rights reserved.
//


import SwiftUI
import Foundation
import Combine

 /*
struct Pral: Codable, Identifiable {
    
    public var id: String
   // public var nom: String
   // public var pral: String
    
    enum CodingKeys: String, CodingKey {
        case id = "id"
   //     case nom = "nom"
   //     case pral = "pral"
    }
    
}

public class PralFetcher: ObservableObject {
    
    @Published var prals = [Pral]()
    
    init() {
        load()
    }
    
    func load() {
        let url = URL(string:"https://api.airtable.com/v0/appCbXWHtXH4FHbkL/PRAL?api_key=key91gAS3qYwf6Q4V")!
        URLSession.shared.dataTask(with: url) {
            (data,response,error) in
                do {
                    if let d = data {
                        let decodedLists = try JSONDecoder().decode([Pral].self, from: d)
                        DispatchQueue.main.async {
                            self.prals = decodedLists
                        }
                    } else {
                        print("No Data")
                    }
                } catch {
                    print ("Error")
                }
        }.resume()
    }
}

struct ContentView: View {
    
    @ObservedObject var fetcher = PralFetcher()
    
    var body: some View {
        
        VStack {
            List(fetcher.prals) { p in
                Text(p.id)
                //VStack (alignment: .leading) {
                    //Text(p.id)
                    //Text(pral.nom)
                    //Text(pral.pral)
                    //    .font(.system(size: 11))
                    //    .foregroundColor(Color.gray)
                //}
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

*/


struct Movie: Codable, Identifiable {
    
    public var id: Int
    public var name: String
    public var released: String
    
    enum CodingKeys: String, CodingKey {
        case id = "id"
        case name = "title"
        case released = "year"
    }
    
}

public class MovieFetcher: ObservableObject {
    
    @Published var movies = [Movie]()
    
    init() {
        load()
    }
    
    func load() {
        let url = URL(string:"https://gist.githubusercontent.com/rbreve/60eb5f6fe49d5f019d0c39d71cb8388d/raw/f6bc27e3e637257e2f75c278520709dd20b1e089/movies.json")!
        URLSession.shared.dataTask(with: url) {
            (data,response,error) in
                do {
                    if let d = data {
                        let decodedLists = try JSONDecoder().decode([Movie].self, from: d)
                        DispatchQueue.main.async {
                            self.movies = decodedLists
                        }
                    } else {
                        print("No Data")
                    }
                } catch {
                    print ("Error")
                }
        }.resume()
    }
}

struct ContentView: View {
    
    @ObservedObject var fetcher = MovieFetcher()
    
    var body: some View {
        
        VStack {
            List(fetcher.movies) { movie in
                VStack (alignment: .leading) {
                    Text(movie.name)
                    Text(movie.released)
                        .font(.system(size: 11))
                        .foregroundColor(Color.gray)
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
