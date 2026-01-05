export interface UploadFile {
    mode: string | null;
    name: string | null;
    size: number | null;
    uri?: string | null;
    path?: string | null;
    label?: string | null;
    url?: string | null;
}

/** A secondary file (e.g., index) to be imported alongside the primary file */
export interface SecondaryFileSelection {
    /** Path/URI to the secondary file */
    path: string;
    /** The metadata key this file should be stored under (e.g., "bam_index") */
    metadataKey: string;
    /** Human-readable description of the file type */
    description: string;
    /** Whether this secondary file should be imported */
    selected: boolean;
}

export function isLocalFile(file: unknown): file is File {
    return file !== null && typeof file === "object" && "name" in file && "size" in file;
}

export interface FileStream {
    name: string;
    size: number;
    stream: ReadableStream<Uint8Array>;
    lastModified: number;
    isStream: true;
}

export interface UploadItem {
    dbKey: string;
    deferred?: boolean;
    enabled: boolean;
    extension: string;
    fileContent: string;
    fileData: object | null;
    fileMode: string;
    fileName: string;
    filePath: string;
    fileSize: number;
    fileUri?: string | null;
    info?: string | null;
    optional: boolean;
    outputs: object | null;
    percentage: number;
    /** Secondary files (e.g., indexes) detected and selected for import */
    secondaryFiles?: SecondaryFileSelection[];
    spaceToTab: boolean;
    status: string;
    targetHistoryId?: string;
    toPosixLines: boolean;
    id?: string;
}

export const defaultModel: UploadItem = {
    dbKey: "?",
    deferred: false,
    enabled: true,
    extension: "auto",
    fileContent: "",
    fileData: null,
    fileMode: "",
    fileName: "",
    filePath: "",
    fileSize: 0,
    fileUri: null,
    info: null,
    optional: false,
    outputs: null,
    percentage: 0,
    secondaryFiles: undefined,
    spaceToTab: false,
    status: "init",
    toPosixLines: true,
};
