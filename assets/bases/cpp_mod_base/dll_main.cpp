#include <Mod/CppUserModBase.hpp>
#include <DynamicOutput/DynamicOutput.hpp>
#include <Unreal/UObjectGlobals.hpp>
#include <Unreal/UObject.hpp>

using namespace RC;
using namespace RC::Unreal;

class ExampleMod : public CppUserModBase
{
public:
    ExampleMod() : CppUserModBase()
    {
        ModName = STR("Example Mod");
        ModVersion = STR("1.0");
        ModDescription = STR("Example mod description");
        ModAuthors = STR("Example Author Name");
        // Do not change this unless you want to target a UE4SS version
        // other than the one you're currently building with somehow.
        //ModIntendedSDKVersion = STR("x.x");
        
        Output::send<LogLevel::Verbose>(STR("Example mod print out\n"));
    }

    ~ExampleMod() override {}

    auto on_update() -> void override {}

    auto on_unreal_init() -> void override
    {
        auto Object = UObjectGlobals::StaticFindObject<UObject*>(nullptr, nullptr, STR("/Script/CoreUObject.Object"));
        Output::send<LogLevel::Verbose>(STR("Object Name: {}\n"), Object->GetFullName());
    }
};

#define EXAMPLE_MOD_API __declspec(dllexport)
extern "C"
{
    EXAMPLE_MOD_API CppUserModBase* start_mod()
    {
        return new ExampleMod();
    }

    EXAMPLE_MOD_API void uninstall_mod(CppUserModBase* mod)
    {
        delete mod;
    }
}