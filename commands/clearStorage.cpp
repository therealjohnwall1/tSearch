#include <fstream>
#include <filesystem>

using namespace std;

void clear(){
    std::filesystem::path paf = "../util/storage";

    if (std::filesystem::exists(paf)) {
        std::filesystem::remove_all(paf);
  }
}
int main(){
    clear();
    return 0;
}

//needs gcc 17 , redo it later