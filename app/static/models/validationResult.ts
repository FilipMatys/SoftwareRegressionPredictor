export interface ValidationResult {
    data: any,
    errors: string[],
    warnings: string[],
    isValid: boolean
}