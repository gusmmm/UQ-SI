# Guide to LLM Classification of Medical Texts: Burn Etiology

This guide outlines the standard classification of burn injuries based on etiology, as used in medical texts, to aid in Large Language Model (LLM) classification tasks.

## Goal

To enable the LLM to accurately categorize medical texts related to burns based on their causative agent (etiology).

## Classification of Burns by Etiology

The primary classification of burns is based on the **mechanism of injury**, divided into the following categories:

### 1. Thermal Burns

This is the most prevalent category and is further broken down into:

*   **Scald:**
    *   **Definition:** Caused by contact with hot liquids or steam.
    *   **Keywords:** hot water, boiling liquid, steam, hot oil.
    *   **Context:** Common in children and older adults. Often involves spills or immersion.
*   **Flame:**
    *   **Definition:** Caused by direct contact with flames.
    *   **Keywords:** fire, open flame, ignited clothing, house fire, explosion (if involving burning fuel).
    *   **Context:** Associated with house fires, flammable liquids, and accidents involving open flames.
*   **Contact:**
    *   **Definition:** Caused by contact with hot solid objects.
    *   **Keywords:** hot metal, stove, iron, hot surface, heater.
    *   **Context:** Can occur in various settings, including homes and industrial environments.
*   **Flash:**
    *   **Definition:** Caused by brief exposure to intense heat, typically from an explosion.
    *   **Keywords:** explosion, blast, intense heat, brief exposure.
    *   **Context:** Often associated with explosions and may result in superficial burns over a large area.

### 2. Chemical Burns

*   **Definition:** Caused by contact with corrosive substances.
*   **Keywords:** acid, alkali, lye, caustic, chemical spill, (specific chemical names like) sulfuric acid, hydrochloric acid, sodium hydroxide.
*   **Context:** Severity depends on chemical type, concentration, and duration of contact. Requires immediate irrigation.

### 3. Electrical Burns

*   **Definition:** Caused by electric current passing through the body.
*   **Keywords:** electric shock, electrical current, high voltage, low voltage, power line, lightning strike, arc, flash burn (in the case of a high-voltage arc).
    * **High Voltage**
    * **Low Voltage**
    * **Arc Flash**
*   **Context:** Often causes internal damage, even with small surface burns. Cardiac monitoring is crucial.

### 4. Radiation Burns

*   **Definition:** Caused by exposure to ionizing radiation or extensive UV radiation.
*   **Keywords:** radiation, radiotherapy, nuclear, UV, ultraviolet, sunburn (if severe).
*   **Context:** Can occur from medical treatments, industrial accidents, or prolonged sun exposure.

### 5. Friction Burns

*   **Definition:** Caused by skin rubbing against a rough surface at high speed.
*   **Keywords:** road rash, abrasion, friction, rug burn.
*   **Context:** Commonly seen in road traffic accidents, falls, or sports injuries.
