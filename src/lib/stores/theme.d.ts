import { Writable } from 'svelte/store';

// Export the theme store type
export declare const theme: Writable<string>;

// Export function declarations
export declare function toggleTheme(): void;
export declare function initTheme(): void;
