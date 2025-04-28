package com.pham_mishra.parisairline.service;

import com.pham_mishra.parisairline.model.Plane;
import com.pham_mishra.parisairline.repository.PlaneRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PlaneService {

    private final PlaneRepository planeRepository;

    @Autowired
    public PlaneService(PlaneRepository planeRepository) {
        this.planeRepository = planeRepository;
    }

    public List<Plane> getAllPlanes() {
        return planeRepository.findAll();
    }

    public Optional<Plane> getPlaneById(Long id) {
        return planeRepository.findById(id);
    }

    public Plane addPlane(Plane plane) {
        return planeRepository.save(plane);
    }

    public Plane updatePlane(Long id, Plane updatedPlane) {
        return planeRepository.findById(id).map(plane -> {
            if (updatedPlane.getPlaneBrand() != null) {
                plane.setPlaneBrand(updatedPlane.getPlaneBrand());
            }
            if (updatedPlane.getPlaneModel() != null) {
                plane.setPlaneModel(updatedPlane.getPlaneModel());
            }
            if (updatedPlane.getPlaneManufacturer() != null) {
                plane.setPlaneManufacturer(updatedPlane.getPlaneManufacturer());
            }
            return planeRepository.save(plane);
        }).orElse(null);
    }

    public void deletePlane(Long id) {
        planeRepository.deleteById(id);
    }

}
