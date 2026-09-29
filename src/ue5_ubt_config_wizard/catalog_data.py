"""Public API identifiers observed in Epic's UE 5.8 documentation.

Checked 2026-09-29. This is a documentation inventory, not an engine compatibility
certificate. Descriptions and types are deliberately not guessed from names.
"""

DOCUMENTED_VERSION = "5.8"
RETRIEVED = "2026-09-29"
SOURCE = (
    "https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine"
)

DOCUMENTED_SETTINGS = (
    ("BuildConfiguration", "bIgnoreOutdatedImportLibraries"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPrintDebugInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowHybridExecutor"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "RemoteExecutorPriority"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowUBAExecutor"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowUBALocalExecutor"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowXGE"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowFASTBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowSNDBS"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseUBTMakefiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MaxParallelActions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllCores"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCompactOutput"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bArtifactRead"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bArtifactWrites"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bLogArtifactCacheMisses"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ArtifactDirectory"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseUnityBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bForceUnityBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bParallelMakefileGeneration"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "UnsafeTypeCastWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "UndefinedIdentifierWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "UnreachableCodeWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "SwitchUnhandledEnumeratorWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ShortenSizeTToIntWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DeprecationWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "PCHPerformanceIssueWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ModuleUnsupportedWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "PluginModuleUnsupportedWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ModuleIncludePathWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ModuleIncludePrivateWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ModuleIncludeSubdirectoryWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DefaultWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bShowIncludes"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDebugBuildsActuallyUseDebugCRT"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bLegalToDistributeBinary"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bBuildAllModules"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseVerseBPVM"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bForceNoAutoRTFMCompiler"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseAutoRTFMVerifier"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAutoRTFMVerify"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAutoRTFMClosedStaticLinkage"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAutoRTFMRedirectionInstrumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseInlining"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bWithLiveCoding"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseDebugLiveCodingConsole"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseSparseSetStrictMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseCompactSetAsDefault"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseXGEController"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bIncludeHeaders"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAlwaysUseUnityForGeneratedFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseAdaptiveUnityBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityDisablesOptimizations"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "AdaptiveUnityDisablesOptimizationsConfigurations"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityDisablesPCH"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityDisablesProjectPCHForProjectPrivate"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityCreatesDedicatedPCH"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityEnablesEditAndContinue"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAdaptiveUnityCompilesHeaderFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MinGameModuleSourceFilesForUnityBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bRequireObjectPtrForAddReferencedObjects"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bValidateFormatStrings"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bWarningsAsErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bRetainFramePointers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseFastMonoCalls"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "NumIncludedBytesPerUnityCPP"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableModuleNumIncludedBytesPerUnityCPPOverride"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStressTestUnity"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DebugInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DebugInfoLineTablesOnly"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DebugInfoNoInlineLineTables"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "DebugInfoSimpleTemplateNames"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableDebugInfoForGeneratedCode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bOmitPCDebugInfoInDevelopment"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUsePDBFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUsePCHFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDeterministic"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseVFS"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "CacheSalt"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bChainPCHs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bForceIncludePCHHeadersForGenCppFilesWhenPCHIsDisabled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "StaticAnalyzer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "StaticAnalyzerOutputType"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "StaticAnalyzerMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "StaticAnalyzerPVSPrintLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStaticAnalyzerProjectOnly"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStaticAnalyzerIncludeGenerated"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MinFilesUsingPrecompiledHeader"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bForcePrecompiledHeaderForGameModules"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseIncrementalLinking"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowLTCG"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPreferThinLTO"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ThinLTOCacheDirectory"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ThinLTOCachePruningArguments"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bThinLTODistributed"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPGOProfile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPGOOptimize"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCodeCoverage"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bSupportEditAndContinue"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bOmitFramePointers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bShaderCompilerWorkerTrace"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseSharedPCHs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseShippingPhysXLibraries"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseCheckedPhysXLibraries"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCheckLicenseViolations"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bBreakBuildOnLicenseViolation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCreateMapFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAllowRuntimeSymbolFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "PackagePath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "CrashDiagnosticDirectory"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCheckSystemHeadersForModification"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableLinking"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bFlushBuildDirOnRemoteMac"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPrintToolChainTimingInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bParseTimingInfoForTracing"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPublicSymbolsByDefault"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MSVCCompileActionWeight"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "ClangCompileActionWeight"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "CppStandardEngine"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "CppStandard"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "CStandard"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MinCpuArchX64"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bMinCpuArchAPX"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "MinArm64CpuTarget"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDetailedUnityFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableDebugInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUndefinedIdentifierErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bPrioritizeDependencyScanning"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStopSNDBSCompilationAfterErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bXGENoWatchdogThread"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bShowXGEMonitor"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStopXGECompilationAfterErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bShowTimeline"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "TempDirectory"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDeleteTempDirectory"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseIpv6"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "BaseLogFileName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "IWYUBaseLogFileName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bStripSymbols"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bCreateStripFlagFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bSkipClangValidation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableAddressSanitizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableThreadSanitizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableUndefinedBehaviorSanitizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUsePortableToolchain"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUseDSYMFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableLibFuzzer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableMemorySanitizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableAutoRTFMSanitizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bTuneDebugInfoForLLDB"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableDumpSyms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bDisableStripSymbols"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bLinuxSampleBasedPGO"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEnableInstrumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bWriteSolutionOptionFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bVsConfigFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bAddFastPDBToProjects"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bUsePerFileIntellisense"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildConfiguration", "bEditorDependsOnShaderCompileWorker"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bForceHeaderGeneration"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bEnableUHTInputCache"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bDoNotBuildUHT"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bFailIfGeneratedCodeChanges"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bAllowHotReloadFromIDE"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bForceDebugUnrealHeaderTool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bUseBuiltInUnrealHeaderTool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UEBuildConfiguration", "bWarnOnCppUnrealHeaderTool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "MaxRootPathLength"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "MaxNestedPathLength"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bIgnoreStalePGOData"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bUseFastGenProfile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "PreMergedPgdFilename"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bPGONoExtraCounters"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bSampleBasedPGO"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "DefaultPreferredCompilers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "CompilerVersion"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "ToolchainVersion"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bVCFastFail"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bVCExtendedWarningInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bClangStandaloneDebug"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bAllowClangLinker"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bAllowRadLinker"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "WindowsSdkVersion"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bWriteSarif"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bStripPrivateSymbols"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bNoLinkerDebugInfo"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "PCHMemoryAllocationFactor"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "AdditionalLinkerOptions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bSyntaxCheckOnly"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bReducedOptimizeHugeFunctions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "ReducedOptimizeHugeFunctionsThreshold"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bClangTimeTrace"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bCompilerTrace"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bSetResourceVersions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "InlineFunctionExpansionLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bDynamicDebugging"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "Compiler"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "ToolChain"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "PreferredCompilers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "ToolchainVersionWarningLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bStrictConformanceMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bUpdatedCPPMacro"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bStrictInlineConformance"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bStrictEnumTypesConformance"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bStrictODRViolationConformance"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bDisableVolatileMetadata"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "StructMemberAlignment"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bConfigureVSRemoteDebugger"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "RemoteWinRoot"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "RemoteDebugMachineX64"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "RemoteDebugMachineArm64"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsPlatform", "bRemoteDebuggerAuthentication"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "DisableMergingModuleAndGeneratedFilesInUnityFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "DisableUnityBuild"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "EnableOptimizeCode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "DisableOptimizeCode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "OptimizeForSize"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ModuleConfiguration", "OptimizeForSizeAndSpeed"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TargetRules", "bCompileChaosVisualDebuggerSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TargetRules", "bCompileRewindDebuggerSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TargetRules", "bCompileAsioSSLSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bStoreObjFilesCompressed"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "Cache"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "WriteCache"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "RequireVFS"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheCrypto"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheDesiredConnectionCount"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "Providers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "BuildMachineProviders"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheProviders"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "BuildMachineCacheProviders"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDisableRemote"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bForceBuildAllRemote"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bAllowRetry"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bForcedRetry"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bForcedRetryRemote"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bStrict"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bStoreRaw"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bLinkRemote"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "StoreCapacityGb"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "MaxWorkers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "SendSize"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "Host"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "Port"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "RootDir"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bUseQuic"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bLogEnabled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bPrintSummary"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bLaunchVisualizer"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bResetCas"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "TraceFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDetailedTrace"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDisableWaitOnMem"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bAllowKillOnMem"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bWriteToDisk"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDisableCustomAlloc"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "Zone"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bUseCrypto"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bUseKnownInputs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "ActionsOutputFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDetailedLog"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "AllowDetour"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "WritePlaceholders"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "SharedMemoryTempFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "MaxRacingPercent"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheMaxWorkers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheShuffle"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "ForceNoCache"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "ReportCacheMissReason"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CacheLinkActions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "CompressionLevel"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("UnrealBuildAccelerator", "bDisableHorde"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TestTargetRules", "bCompileChaosVisualDebuggerSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TestTargetRules", "bCompileRewindDebuggerSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("TestTargetRules", "bCompileAsioSSLSupport"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "FBuildExecutablePath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "bEnableDistribution"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "FBuildBrokeragePath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "FBuildCoordinator"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "bEnableCaching"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "CacheMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "FBuildCachePath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "bForceRemote"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "bStopOnError"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "MsvcCRTRedistVersion"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("FASTBuild", "CompilerVersion"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("SNDBS", "bAllowOverVpn"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("SNDBS", "VpnSubnets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "ProcessorCountMultiplier"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "MemoryPerActionBytes"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "ProcessPriority"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bStopCompilationAfterErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "StopCompilationAfterNumErrors"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bShowCompilationTimes"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bShowPerActionCompilationTimes"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bLogActionCommandLines"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bPrintActionTargetNames"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ParallelExecutor", "bShowCPUUtilization"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Server"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Token"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "OidcProvider"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Pool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "LinuxPool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "MacPool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "WindowsPool"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Requirements"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Cluster"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "LocalHost"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "MaxCores"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "MaxWorkers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "MaxIdle"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "StartupDelay"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "AllowWine"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "ConnectionMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "Encryption"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "UBASentryUrl"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "AgentPlatform"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Horde", "VerboseAuthLogging"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "bAllowOverVpn"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "VpnSubnets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "bAllowRemoteLinking"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "bUseVCCompilerMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "MinActions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XGE", "bUnavailableIfInUse"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Log", "bBackupLogFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Log", "LogFileBackupCount"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("Telemetry", "Providers"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("BuildMode", "bIgnoreJunk"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "DisablePlatformProjectGenerators"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "Format"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bGenerateIntelliSenseData"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bAllDocumentationLanguages"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeBuildSystemFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeLocalizationFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bKeepSourceSubDirectories"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "Platforms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "Configurations"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bGatherThirdPartySource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeTestAndShippingConfigs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeDebugConfigs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bIncludeDevelopmentConfigs"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("ProjectFileGenerator", "bVisualStudioLinux"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RemoteMac", "ServerName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RemoteMac", "UserName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RemoteMac", "SshPrivateKey"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RemoteMac", "RsyncAuthentication"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RemoteMac", "SshAuthentication"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("IOSToolChain", "bUseDangerouslyFastMode"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("WindowsTargetRules", "ObjSrcMapFile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("AndroidStudioFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CLionGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CMakefileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("CodeLiteGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("EddieProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("KDevelopGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("MakefileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("QMakefileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("RiderProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "IncludeAllFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "AddDebugAttachConfig"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "AddDebugCoreConfig"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "NoCompileCommands"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "UseVSCodeExtension"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "LinuxDebuggerType"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSCodeProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VSWorkspaceProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "Version"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "MaxSharedIncludePaths"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "ExcludedIncludePaths"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "ExcludedFilePaths"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bBuildUBTInDebug"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bHeadersAsClCompile"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bBuildLiveCodingConsole"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bMakeProjectPerTarget"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("VCProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeDocumentation"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bUsePrecompiled"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeEngineSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeShaderSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeConfigFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeTemplateFiles"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeEnginePrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "IncludeCppSource"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeDotNetPrograms"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bIncludeTempTargets"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "PrimaryProjectName"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bPrimaryProjectNameFromFolder"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("XcodeProjectFileGenerator", "bPrimaryProjectNameAppendDriveLetter"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("SourceFileWorkingSet", "Provider"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("SourceFileWorkingSet", "RepositoryPath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("SourceFileWorkingSet", "GitPath"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("GDKPlatform", "ContentOnlyDebugProject"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("GDKPlatform", "bVerifyLibGDKEditions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
    ("GDKPlatform", "bVerifyDLLGDKEditions"),
    # Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
)
