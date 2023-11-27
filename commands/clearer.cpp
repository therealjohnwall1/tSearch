#include <iostream>
#include <filesystem>
//g++ -std=c++17 need to use 17 compiler or won't work
int main(){
   std::filesystem::path storage = "../util/storage";
   std::filesystem::remove_all(storage);
   std::filesystem::create_directory("../util/storage");

    return 0;
}
