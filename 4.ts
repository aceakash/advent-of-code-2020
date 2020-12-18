import {readFileSync} from 'fs'

console.log(problem1())
console.log(problem2())

function parseRecord(str: string): object {
    const fieldStrings = str.trim()
        .split('\n')
        .map(fl => fl.trim().split(' '))
        .reduce((prev, curr) => {
            return prev.concat(curr)    
        }, [])
    
    const fields: object = {}
    fieldStrings.forEach(fs => {
        const parts = fs.split(':')
        fields[parts[0]] = parts[1]
    })
    return fields
}

function hasAllRequiredFields(record: object): boolean {
    const invalids = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        .filter(rf => record[rf] == null)
    return invalids.length == 0
}

function allFieldsAreValid(record: object): boolean {
    const isNumber = (str: string) => /^\d+$/.test(str)
    const isInRange = (num: number, min: number, max: number) => 
        num >= min && num <= max
    const isValidYear = (fieldName: string, min: number, max: number) => {
        const yearStr = record[fieldName]
        return isNumber(yearStr) &&  isInRange(parseInt(yearStr), min, max)
    }
    if (!isValidYear('byr', 1920, 2002)) return false
    if (!isValidYear('iyr', 2010, 2020)) return false
    if (!isValidYear('eyr', 2020, 2030)) return false

    // height
    const height = record['hgt']
    if (!(/^\d+(cm|in)$/.test(height))) return false
    const unit = height.substr(height.length-2)
    const heightMeasure = Number.parseInt(height.split(unit)[0])
    if (unit === 'cm' && !isInRange(heightMeasure, 150, 193)) {
        return false
    }
    if (unit === 'in' && !isInRange(heightMeasure, 59, 76)) {
        return false
    }

    if (!(/^#[0-9a-f]{6}$/.test(record['hcl']))) return false

    if (!(/^(amb|blu|brn|gry|grn|hzl|oth)$/.test(record['ecl']))) return false

    if (!(/^\d{9}$/.test(record['pid']))) return false
    
    return true
}

function parseInput(filePath: string): object[] {
    return readFileSync(filePath).toString()
        .trim().split('\n\n')
        .map(parseRecord)
        .filter(x => x !== null)
}

function problem1() {
    return parseInput('./4.input.txt')
        .filter(hasAllRequiredFields)
        .length
}

function problem2() {
    return parseInput('./4.input.txt')
        .filter(hasAllRequiredFields)
        .filter(allFieldsAreValid)
        .length
}
