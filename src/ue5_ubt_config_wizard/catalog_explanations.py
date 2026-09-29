"""Original, concise explanations checked against Epic's UE 5.8 guide.

These explain behavior only. They do not establish an XML value type, default,
or support in the user's installed engine. Each entry links to the official
reference through the catalog's source field.

Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
"""

EXPLANATIONS = {
    (
        "BuildConfiguration",
        "bIgnoreOutdatedImportLibraries",
    ): "Skip relinking solely because a dependent import library is older than its inputs; this can speed up iteration.",
    (
        "BuildConfiguration",
        "bAllowHybridExecutor",
    ): "Select the hybrid local and remote executor. Epic marks this executor as no longer supported.",
    (
        "BuildConfiguration",
        "RemoteExecutorPriority",
    ): "Set the preference order among XGE, SN-DBS, FASTBuild, and UBA remote executors.",
    ("BuildConfiguration", "bAllowSNDBS"): "Allow SN-DBS as a build executor when it is available.",
    (
        "BuildConfiguration",
        "bAllCores",
    ): "Include logical CPU cores when UBT calculates the number of available cores.",
    (
        "BuildConfiguration",
        "bLogArtifactCacheMisses",
    ): "Write informational log entries for artifact-cache misses.",
    (
        "BuildConfiguration",
        "ArtifactDirectory",
    ): "Choose the directory used to store build artifacts.",
    (
        "BuildConfiguration",
        "bForceUnityBuild",
    ): "Require eligible C++ source files to be combined into unity translation units.",
    (
        "BuildConfiguration",
        "bParallelMakefileGeneration",
    ): "Generate target makefiles concurrently.",
    (
        "BuildConfiguration",
        "UnsafeTypeCastWarningLevel",
    ): "Control the diagnostic level for potentially unsafe type conversions.",
    (
        "BuildConfiguration",
        "UndefinedIdentifierWarningLevel",
    ): "Control diagnostics for undefined names in preprocessor conditions.",
    (
        "BuildConfiguration",
        "UnreachableCodeWarningLevel",
    ): "Control diagnostics for code that cannot be reached.",
    (
        "BuildConfiguration",
        "SwitchUnhandledEnumeratorWarningLevel",
    ): "Control diagnostics for switch statements that omit enumeration members.",
    (
        "BuildConfiguration",
        "ShortenSizeTToIntWarningLevel",
    ): "Control diagnostics when converting size_t to a narrower integer type.",
    (
        "BuildConfiguration",
        "DeprecationWarningLevel",
    ): "Control diagnostics for use of deprecated declarations.",
    (
        "BuildConfiguration",
        "PCHPerformanceIssueWarningLevel",
    ): "Control diagnostics about possible precompiled-header performance problems.",
    (
        "BuildConfiguration",
        "ModuleUnsupportedWarningLevel",
    ): "Control diagnostics for unsupported modules.",
    (
        "BuildConfiguration",
        "PluginModuleUnsupportedWarningLevel",
    ): "Control diagnostics for unsupported modules supplied by plugins.",
    (
        "BuildConfiguration",
        "ModuleIncludePathWarningLevel",
    ): "Control validation messages for module include paths.",
    (
        "BuildConfiguration",
        "ModuleIncludePrivateWarningLevel",
    ): "Control messages when a module include path exposes private headers.",
    (
        "BuildConfiguration",
        "ModuleIncludeSubdirectoryWarningLevel",
    ): "Control messages about unnecessary module include subdirectories.",
    (
        "BuildConfiguration",
        "DefaultWarningLevel",
    ): "Set the treatment of warnings that have no more specific level.",
    ("BuildConfiguration", "bShowIncludes"): "Print the header files included by each source file.",
    (
        "BuildConfiguration",
        "bDebugBuildsActuallyUseDebugCRT",
    ): "Use the debug C runtime in debug builds; third-party static libraries may also need debug variants.",
    (
        "BuildConfiguration",
        "bLegalToDistributeBinary",
    ): "Allow public distribution of the target output even when it depends on specially restricted modules.",
    (
        "BuildConfiguration",
        "bBuildAllModules",
    ): "Build every module valid for the target type; Epic notes this for CI and installed-engine builds.",
    ("BuildConfiguration", "bUseVerseBPVM"): "Use BPVM to run Verse.",
    (
        "BuildConfiguration",
        "bForceNoAutoRTFMCompiler",
    ): "Prevent use of the AutoRTFM Clang compiler.",
    ("BuildConfiguration", "bUseAutoRTFMVerifier"): "Emit metadata used for AutoRTFM verification.",
    (
        "BuildConfiguration",
        "bAutoRTFMVerify",
    ): "Run LLVM verification after the AutoRTFM compiler pass.",
    (
        "BuildConfiguration",
        "bAutoRTFMClosedStaticLinkage",
    ): "Link closed function declarations statically for AutoRTFM.",
    (
        "BuildConfiguration",
        "bAutoRTFMRedirectionInstrumentation",
    ): "Instrument memory accesses for AutoRTFM redirection.",
    ("BuildConfiguration", "bUseInlining"): "Enable compiler inlining across modules.",
    ("BuildConfiguration", "bWithLiveCoding"): "Include support for Live Coding in the build.",
    (
        "BuildConfiguration",
        "bUseDebugLiveCodingConsole",
    ): "Enable support for the Live Coding debug console.",
    (
        "BuildConfiguration",
        "bUseSparseSetStrictMode",
    ): "Add runtime checks for sparse-set usage that conflicts with compact sets.",
    (
        "BuildConfiguration",
        "bUseCompactSetAsDefault",
    ): "Use TCompactSet instead of TSparseSet as the default TSet backing container.",
    (
        "BuildConfiguration",
        "bUseXGEController",
    ): "Include the XGE controller components needed for distributed shader compilation.",
    (
        "BuildConfiguration",
        "bIncludeHeaders",
    ): "Include header files from included modules in the build.",
    (
        "BuildConfiguration",
        "bAlwaysUseUnityForGeneratedFiles",
    ): "Place generated source files into a unity file even when regular unity builds are off.",
    (
        "BuildConfiguration",
        "bUseAdaptiveUnityBuild",
    ): "Keep files being actively edited out of unity blobs to improve incremental compile times.",
    (
        "BuildConfiguration",
        "AdaptiveUnityDisablesOptimizationsConfigurations",
    ): "Choose configurations where adaptive non-unity files compile without optimization.",
    (
        "BuildConfiguration",
        "bAdaptiveUnityDisablesPCH",
    ): "Avoid forced precompiled headers for files in the adaptive working set.",
    (
        "BuildConfiguration",
        "bAdaptiveUnityDisablesProjectPCHForProjectPrivate",
    ): "Stores the adaptive-unity project-PCH setting for private project code.",
    (
        "BuildConfiguration",
        "bAdaptiveUnityCreatesDedicatedPCH",
    ): "Create a separate precompiled header for each source file in the adaptive working set.",
    (
        "BuildConfiguration",
        "bAdaptiveUnityEnablesEditAndContinue",
    ): "Prepare adaptive working-set files for Edit and Continue using dedicated PCHs.",
    (
        "BuildConfiguration",
        "bAdaptiveUnityCompilesHeaderFiles",
    ): "Compile working-set headers through generated source files to catch missing includes.",
    (
        "BuildConfiguration",
        "MinGameModuleSourceFilesForUnityBuild",
    ): "Set the game-module source-file count at which unity compilation begins.",
    (
        "BuildConfiguration",
        "bRequireObjectPtrForAddReferencedObjects",
    ): "Require TObjectPtr use with FReferenceCollector for incremental-GC compatibility.",
    (
        "BuildConfiguration",
        "bValidateFormatStrings",
    ): "Produce compile errors for invalid UE_LOG format strings.",
    (
        "BuildConfiguration",
        "bWarningsAsErrors",
    ): "Treat all compiler warnings as errors, including categories UE normally exempts.",
    (
        "BuildConfiguration",
        "bRetainFramePointers",
    ): "Keep frame pointers to support reliable call stacks and memory profiling.",
    (
        "BuildConfiguration",
        "NumIncludedBytesPerUnityCPP",
    ): "Target this approximate amount of C++ source text in each unity file.",
    (
        "BuildConfiguration",
        "bDisableModuleNumIncludedBytesPerUnityCPPOverride",
    ): "Ignore module-specific overrides of the unity-file size target.",
    (
        "BuildConfiguration",
        "bStressTestUnity",
    ): "Compile the project's C++ source through one unity file to expose unity-build issues.",
    (
        "BuildConfiguration",
        "DebugInfo",
    ): "Choose how much debug information the compiler generates; see Epic's DebugInfoMode reference.",
    (
        "BuildConfiguration",
        "DebugInfoLineTablesOnly",
    ): "Limit supported compilers' debug output to line tables.",
    (
        "BuildConfiguration",
        "DebugInfoNoInlineLineTables",
    ): "Omit line tables for inline functions when the compiler supports it.",
    (
        "BuildConfiguration",
        "DebugInfoSimpleTemplateNames",
    ): "Shorten template type names in supported compilers' debug information.",
    (
        "BuildConfiguration",
        "bDisableDebugInfoForGeneratedCode",
    ): "Skip debug information for generated source to reduce link time and PDB size.",
    (
        "BuildConfiguration",
        "bOmitPCDebugInfoInDevelopment",
    ): "Skip debug information in PC and Mac development builds for faster iteration.",
    (
        "BuildConfiguration",
        "bUsePDBFiles",
    ): "Generate PDB debug-symbol files for Visual C++ builds.",
    ("BuildConfiguration", "bUsePCHFiles"): "Use precompiled headers during compilation.",
    (
        "BuildConfiguration",
        "bDeterministic",
    ): "Use deterministic compiler and linker flags; MSVC compilation may slow down.",
    (
        "BuildConfiguration",
        "bUseVFS",
    ): "Try experimental toolchain virtual-file-system support for consistent output paths.",
    (
        "BuildConfiguration",
        "CacheSalt",
    ): "Change cache-bucket calculation to invalidate cached action outputs.",
    ("BuildConfiguration", "bChainPCHs"): "Chain precompiled headers when using Clang.",
    (
        "BuildConfiguration",
        "bForceIncludePCHHeadersForGenCppFilesWhenPCHIsDisabled",
    ): "Force-include PCH headers for generated C++ when normal PCH use is off.",
    (
        "BuildConfiguration",
        "StaticAnalyzer",
    ): "Select whether static code analysis runs during the build.",
    (
        "BuildConfiguration",
        "StaticAnalyzerOutputType",
    ): "Select the output format for Clang static analysis.",
    (
        "BuildConfiguration",
        "StaticAnalyzerMode",
    ): "Select Clang static-analysis depth; shallow analysis is faster.",
    (
        "BuildConfiguration",
        "StaticAnalyzerPVSPrintLevel",
    ): "Set the PVS-Studio warning level printed during static analysis.",
    (
        "BuildConfiguration",
        "bStaticAnalyzerProjectOnly",
    ): "Analyze project modules while skipping engine modules.",
    (
        "BuildConfiguration",
        "bStaticAnalyzerIncludeGenerated",
    ): "Include generated source files in static analysis.",
    (
        "BuildConfiguration",
        "MinFilesUsingPrecompiledHeader",
    ): "Require this many source files to use a header before UBT creates its PCH.",
    (
        "BuildConfiguration",
        "bForcePrecompiledHeaderForGameModules",
    ): "Generate PCHs for game modules even when only a few source files use them.",
    (
        "BuildConfiguration",
        "bUseIncrementalLinking",
    ): "Enable incremental linking to shorten small rebuilds; Epic notes possible reliability issues.",
    ("BuildConfiguration", "bAllowLTCG"): "Allow link-time code generation.",
    (
        "BuildConfiguration",
        "bPreferThinLTO",
    ): "Prefer the lighter ThinLTO mode where link-time optimization is supported.",
    (
        "BuildConfiguration",
        "ThinLTOCacheDirectory",
    ): "Choose the ThinLTO cache directory on supported platforms.",
    (
        "BuildConfiguration",
        "ThinLTOCachePruningArguments",
    ): "Set ThinLTO cache-pruning arguments when a cache directory is configured.",
    (
        "BuildConfiguration",
        "bThinLTODistributed",
    ): "Use distributed linking for ThinLTO when supported.",
    (
        "BuildConfiguration",
        "bPGOProfile",
    ): "Build with profile-guided optimization instrumentation.",
    (
        "BuildConfiguration",
        "bPGOOptimize",
    ): "Optimize the build using profile-guided optimization data.",
    (
        "BuildConfiguration",
        "bCodeCoverage",
    ): "Compile and link the target with code-coverage support.",
    (
        "BuildConfiguration",
        "bSupportEditAndContinue",
    ): "Enable compiler support for Edit and Continue.",
    (
        "BuildConfiguration",
        "bOmitFramePointers",
    ): "Omit frame pointers; disabling this can help PC memory profiling.",
    (
        "BuildConfiguration",
        "bShaderCompilerWorkerTrace",
    ): "Enable Unreal Insights tracing in Shader Compiler Worker.",
    (
        "BuildConfiguration",
        "bUseSharedPCHs",
    ): "Share selected precompiled headers between modules to reduce compile time.",
    (
        "BuildConfiguration",
        "bCheckLicenseViolations",
    ): "Check whether built modules violate Epic's distribution restrictions.",
    (
        "BuildConfiguration",
        "bBreakBuildOnLicenseViolation",
    ): "Fail a build when the license-violation check finds a problem.",
    ("BuildConfiguration", "bCreateMapFile"): "Emit a linker map file as a build output.",
    (
        "BuildConfiguration",
        "bAllowRuntimeSymbolFiles",
    ): "Generate symbol files used to resolve runtime call-stack names on supported platforms.",
    (
        "BuildConfiguration",
        "PackagePath",
    ): "Choose where to save linker input files for link-crash investigation.",
    (
        "BuildConfiguration",
        "CrashDiagnosticDirectory",
    ): "Choose the directory for supported platforms' crash reports.",
    (
        "BuildConfiguration",
        "bCheckSystemHeadersForModification",
    ): "Check system headers for changes when deciding which actions are outdated.",
    ("BuildConfiguration", "bDisableLinking"): "Skip the linking step for this target.",
    (
        "BuildConfiguration",
        "bFlushBuildDirOnRemoteMac",
    ): "Clean the Builds directory on a remote Mac before a build.",
    (
        "BuildConfiguration",
        "bPrintToolChainTimingInfo",
    ): "Request detailed compiler and linker timing output.",
    (
        "BuildConfiguration",
        "bParseTimingInfoForTracing",
    ): "Convert tool timing data into a trace viewable with chrome://tracing.",
    (
        "BuildConfiguration",
        "bPublicSymbolsByDefault",
    ): "Make symbols public by default on POSIX platforms.",
    (
        "BuildConfiguration",
        "MSVCCompileActionWeight",
    ): "Set the CPU and memory scheduling weight of an MSVC compile action.",
    (
        "BuildConfiguration",
        "ClangCompileActionWeight",
    ): "Set the CPU and memory scheduling weight of a Clang compile action.",
    (
        "BuildConfiguration",
        "CppStandardEngine",
    ): "Choose the C++ language standard for engine modules.",
    (
        "BuildConfiguration",
        "CppStandard",
    ): "Choose the C++ language standard for non-engine modules.",
    ("BuildConfiguration", "CStandard"): "Choose the C language standard for the target.",
    (
        "BuildConfiguration",
        "bUndefinedIdentifierErrors",
    ): "Treat undefined names in preprocessor conditions as errors.",
    (
        "BuildConfiguration",
        "bPrioritizeDependencyScanning",
    ): "Give dependency scanning priority over local build jobs.",
    (
        "BuildConfiguration",
        "bStopSNDBSCompilationAfterErrors",
    ): "Stop SN-DBS compilation when a compile error occurs.",
    ("BuildConfiguration", "bShowXGEMonitor"): "Display the XGE build monitor.",
    (
        "BuildConfiguration",
        "bStopXGECompilationAfterErrors",
    ): "Stop XGE compilation after a compile error.",
    (
        "BuildConfiguration",
        "bShowTimeline",
    ): "Show a successful UBT run's execution timeline; failed runs log it quietly.",
    (
        "BuildConfiguration",
        "TempDirectory",
    ): "Use this directory as the base for per-process temporary directories.",
    (
        "BuildConfiguration",
        "bDeleteTempDirectory",
    ): "Delete the application's temporary directory on exit when running one instance.",
    (
        "BuildConfiguration",
        "bUseIpv6",
    ): "Use IPv6 for telemetry and Horde connections where the network supports it.",
    ("BuildConfiguration", "BaseLogFileName"): "Choose the main log file name.",
    ("BuildConfiguration", "IWYUBaseLogFileName"): "Choose the include-what-you-use log file name.",
    ("BuildConfiguration", "bStripSymbols"): "Strip symbol information from build output.",
    (
        "BuildConfiguration",
        "bCreateStripFlagFile",
    ): "Write a .stripped marker file when symbols are stripped.",
}
