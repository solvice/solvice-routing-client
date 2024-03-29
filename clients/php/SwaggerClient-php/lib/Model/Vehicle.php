<?php
/**
 * Vehicle
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Solvice API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0-oas3
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.8
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * Vehicle Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class Vehicle implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Vehicle';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'name' => 'string',
'startlocation' => 'string',
'endlocation' => 'string',
'capacity' => 'BigDecimal',
'capacity2' => 'BigDecimal',
'shiftstart' => 'int',
'shiftend' => 'int',
'type' => 'string[]'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'name' => null,
'startlocation' => null,
'endlocation' => null,
'capacity' => null,
'capacity2' => null,
'shiftstart' => null,
'shiftend' => null,
'type' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'name' => 'name',
'startlocation' => 'startlocation',
'endlocation' => 'endlocation',
'capacity' => 'capacity',
'capacity2' => 'capacity2',
'shiftstart' => 'shiftstart',
'shiftend' => 'shiftend',
'type' => 'type'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'name' => 'setName',
'startlocation' => 'setStartlocation',
'endlocation' => 'setEndlocation',
'capacity' => 'setCapacity',
'capacity2' => 'setCapacity2',
'shiftstart' => 'setShiftstart',
'shiftend' => 'setShiftend',
'type' => 'setType'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'name' => 'getName',
'startlocation' => 'getStartlocation',
'endlocation' => 'getEndlocation',
'capacity' => 'getCapacity',
'capacity2' => 'getCapacity2',
'shiftstart' => 'getShiftstart',
'shiftend' => 'getShiftend',
'type' => 'getType'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['name'] = isset($data['name']) ? $data['name'] : null;
        $this->container['startlocation'] = isset($data['startlocation']) ? $data['startlocation'] : null;
        $this->container['endlocation'] = isset($data['endlocation']) ? $data['endlocation'] : null;
        $this->container['capacity'] = isset($data['capacity']) ? $data['capacity'] : null;
        $this->container['capacity2'] = isset($data['capacity2']) ? $data['capacity2'] : null;
        $this->container['shiftstart'] = isset($data['shiftstart']) ? $data['shiftstart'] : null;
        $this->container['shiftend'] = isset($data['shiftend']) ? $data['shiftend'] : null;
        $this->container['type'] = isset($data['type']) ? $data['type'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['name'] === null) {
            $invalidProperties[] = "'name' can't be null";
        }
        if ($this->container['startlocation'] === null) {
            $invalidProperties[] = "'startlocation' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets name
     *
     * @return string
     */
    public function getName()
    {
        return $this->container['name'];
    }

    /**
     * Sets name
     *
     * @param string $name name
     *
     * @return $this
     */
    public function setName($name)
    {
        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets startlocation
     *
     * @return string
     */
    public function getStartlocation()
    {
        return $this->container['startlocation'];
    }

    /**
     * Sets startlocation
     *
     * @param string $startlocation startlocation
     *
     * @return $this
     */
    public function setStartlocation($startlocation)
    {
        $this->container['startlocation'] = $startlocation;

        return $this;
    }

    /**
     * Gets endlocation
     *
     * @return string
     */
    public function getEndlocation()
    {
        return $this->container['endlocation'];
    }

    /**
     * Sets endlocation
     *
     * @param string $endlocation endlocation
     *
     * @return $this
     */
    public function setEndlocation($endlocation)
    {
        $this->container['endlocation'] = $endlocation;

        return $this;
    }

    /**
     * Gets capacity
     *
     * @return BigDecimal
     */
    public function getCapacity()
    {
        return $this->container['capacity'];
    }

    /**
     * Sets capacity
     *
     * @param BigDecimal $capacity capacity
     *
     * @return $this
     */
    public function setCapacity($capacity)
    {
        $this->container['capacity'] = $capacity;

        return $this;
    }

    /**
     * Gets capacity2
     *
     * @return BigDecimal
     */
    public function getCapacity2()
    {
        return $this->container['capacity2'];
    }

    /**
     * Sets capacity2
     *
     * @param BigDecimal $capacity2 capacity2
     *
     * @return $this
     */
    public function setCapacity2($capacity2)
    {
        $this->container['capacity2'] = $capacity2;

        return $this;
    }

    /**
     * Gets shiftstart
     *
     * @return int
     */
    public function getShiftstart()
    {
        return $this->container['shiftstart'];
    }

    /**
     * Sets shiftstart
     *
     * @param int $shiftstart shiftstart
     *
     * @return $this
     */
    public function setShiftstart($shiftstart)
    {
        $this->container['shiftstart'] = $shiftstart;

        return $this;
    }

    /**
     * Gets shiftend
     *
     * @return int
     */
    public function getShiftend()
    {
        return $this->container['shiftend'];
    }

    /**
     * Sets shiftend
     *
     * @param int $shiftend shiftend
     *
     * @return $this
     */
    public function setShiftend($shiftend)
    {
        $this->container['shiftend'] = $shiftend;

        return $this;
    }

    /**
     * Gets type
     *
     * @return string[]
     */
    public function getType()
    {
        return $this->container['type'];
    }

    /**
     * Sets type
     *
     * @param string[] $type type
     *
     * @return $this
     */
    public function setType($type)
    {
        $this->container['type'] = $type;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}
