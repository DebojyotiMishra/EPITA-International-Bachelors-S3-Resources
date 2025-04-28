package com.pham_mishra.parisairline.service;

import com.pham_mishra.parisairline.model.Airport;
import com.pham_mishra.parisairline.repository.AirportRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class AirportService {

    private final AirportRepository airportRepository;

    @Autowired
    public AirportService(AirportRepository airportRepository) {
        this.airportRepository = airportRepository;
    }

    public List<Airport> getAllAirports() {
        return airportRepository.findAll();
    }

    public Optional<Airport> getAirportById(Long id) {
        return airportRepository.findById(id);
    }

    public Airport saveAirport(Airport airport) {
        return airportRepository.save(airport);
    }

    public Airport updateAirport(Long id, Airport updatedAirport) {
        if (airportRepository.existsById(id)) {
            updatedAirport.setId(id);
            return airportRepository.save(updatedAirport);
        }
        return null;
    }

    public void deleteAirport(Long id) {
        airportRepository.deleteById(id);
    }
}
